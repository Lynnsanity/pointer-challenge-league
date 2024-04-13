from email.message import EmailMessage

import os
import ssl
import smtplib

def send_email(email_sender, email_password, email_receiver, subject, body):
    msg = EmailMessage()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject
    msg.set_content(body, subtype='html')

    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
            print("Sent email successfully.")
            return True
    except Exception as e:
        print("Failed to send email. Check email server settings.", str(e))
        return False



