from email.message import EmailMessage

import os
import ssl
import smtplib
import base64

def send_email(email_sender, email_password, email_receiver, subject, body, image_data=None):
    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.set_content(body, subtype='html')

    context = ssl.create_default_context()

    if image_data:
            image_attachment = base64.b64decode(image_data)
            msg.add_attachment(image_attachment, maintype='image', subtype='png', filename='team_logo.png')
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
            print("Sent email successfully.")
            return True
    except Exception as e:
        print("Failed to send email. Check email server settings.", str(e))
        return False



