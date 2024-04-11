from nicegui import ui
from email.message import EmailMessage

import os
import ssl
import smtplib

def match_registration_received(email_address):

    email_sender = 'somepclemail@info.org'
    email_password = os.environ.get('EMAIL_PASS')
    email_receiver = email_address

    subject = 'Registration Received'
    body = '''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style type="text/css">
          h1{font-size:56px}
          h2{font-size:28px;font-weight:900}
          p{font-weight:100}
          td{vertical-align:top}
          #email{margin:auto;width:600px;background-color:#fff}
        </style>
    </head>
    <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
    <div id="email">
        <table role="presentation" width="100%">
            <tr>
                <td bgcolor="#512698" align="center" style="color: white;">
                    <h1 style="color:#FFC82E">Overwatch 2 PCL 2024 Competition</h1>
                </td>
        </table>
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
            <tr>
                <td>
                    <h2>Thank you for your registration application.</h2>
                    <p>
                        If you are accepted for entry into the competition, you will get another email
                        with information regarding the match.
                    </p>
                    <br>
                    <p>
                        Any changes to the application before *date here* will not be considered for entry.
                        Please make sure to submit any changes before the deadline.
                    </p>
                    <br>
                    <p>
                    Sincerely,
                    <br>
                    The PCL Team
                    </p>
                </td>
            </tr>
        </table>
    </div>
    </body>
    </html>
    '''
    return send_email(
        email_sender=email_sender,
        email_password=email_password,
        email_receiver=email_receiver,
        subject=subject,
        body=body)
    #body = """
    #Game on!
    #Thank you for submitting your PCL registration application for Overwatch 2.

    #If you are accepted for entry into the competition, you will get another email
    #with information regarding the match.

    #If there are changes to your registration, you must contact support with the new
    #information before **deadline here**.
    #"""

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
            print("email sent successfully")
            return True
    except Exception as e:
        print("an error occurred.", str(e))
        return False


