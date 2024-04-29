from components.logic import Enable
from nicegui import ui
from components.sender import send_email

import os

async def contact_submit_click(first_name, last_name, email_address, message_summary):
    enable = Enable()
    fields = {
        "first_name": ("first name", first_name),
        "last_name": ("last name", last_name),
        "email_address": ("email address", email_address),
        "message_summary": ("message summary", message_summary)
    }
    errors = []

    # this for loop takes each field (input) and validates each individually
    # this is so that we can make sure even after they hit submit that it
    # was filled out properly.
    for field, (label, value) in fields.items():
        if not enable.empty(value):
            errors.append(f"Please enter your {label}.")
        elif not field == "message_summary":
            if not enable.char_limit(value):
                errors.append(f"There are too many characters in {label}.")
        elif field == "message_summary":
            if not enable.message_char_limit(value):
                errors.append("There are too many characters in {label}. Max is 512.")
        elif field == "email_address" and not enable.is_valid_email(value):
            errors.append("Please enter a valid email address.")
        else:
            pass

    # if any things went bad in that for loop, we'll notify the user and do nothing else
    if errors:
        for error in errors:
            ui.notify(error, type="error")

    # if there's no errors, send the contact form in an email to uwsp esports
    else:
        contact_email_sent = await contact_message_received(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            message_summary=message_summary)
        # if that email sent then let the user know, if it didn't send then we got a prrrroblem
        if contact_email_sent:
            confirmation_sent = await contact_receipt(
                first_name=first_name,
                last_name=last_name,
                email_address=email_address,
                message_summary=message_summary
            )
            if confirmation_sent:
                ui.notify(f"Successfully sent support ticket. We will get back to you at {email_address} as soon as possible.",
                          type='positive',
                          color='purple-9')
            else:
                ui.notify(f"Successfully sent support ticket. Failed to send receipt.",
                          f"We will get back to you at {email_address} as soon as possible.",
                          type='positive',
                          color='purple-9')
        else:
            ui.notify("Failed to send support ticket."
                      "We are experiencing technical difficulties, please try again later.",
                      type="negative")

# send the user a receipt and some env variables needed to then use sender to send email
async def contact_receipt(first_name, last_name, email_address, message_summary):
    email_sender = 'lynnellesaavedra8@gmail.com'
    email_password = os.environ.get('EMAIL_PASS')
    email_receiver = email_address
    subject = "Contact Support Receipt"
    body = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
    <div id="email">
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
            <tr>
                <td>
                    <h2>PCL OW 2 Support Contact Receipt</h2>
                    <p>
                        Here is your copy of the support ticket submitted.<br>
                        We will get back to you as soon as we can.<br>
                    </p>
                    <p>
                        From: {first_name} {last_name}<br>
                        Email: {email_address}<br>
                        Message: {message_summary}<br>
                    </p>
                    <p>
                    Thank you for your patience,<br>
                    The PCL Team
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

# email to support and some env variables needed to then use sender to send email
async def contact_message_received(first_name, last_name, email_address, message_summary):
    email_sender = 'lynnellesaavedra8@gmail.com'
    email_password = os.environ.get('EMAIL_PASS')
    email_receiver = 'slushiesan99@gmail.com'
    subject = "Contact Support Request"
    body = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body bgcolor="#F5F8FA" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
    <div id="email">
        <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
            <tr>
                <td>
                    <h2>PCL Contact Support Message</h2>
                    <p>
                        From: {first_name} {last_name}<br>
                        Email: {email_address}<br>
                        Message: {message_summary}<br>
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


