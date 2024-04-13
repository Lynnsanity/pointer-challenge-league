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

    # Validate each input individually
    for field, (label, value) in fields.items():
        if not enable.empty(value):
            errors.append(f"Please enter your {label}.")
        elif not enable.char_limit(value):
            if field == "message_summary":
                if not enable.message_char_limit(value):
                    errors.append("There are too many characters in {label}. Max is 512.")
                else:
                    pass
            else:
                errors.append(f"There are too many characters in {label}.")
        elif field == "email_address" and not enable.is_valid_email(value):
            errors.append("Please enter a valid email address.")

    if errors:
        for error in errors:
            ui.notify(error, type="error")
    else:
        email_sent = await contact_message_received(
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
            message_summary=message_summary)

        if email_sent:
            ui.notify(f"Successfully sent ticket. We will get back to you at {email_address} as soon as possible",
                      type='positive',
                      color='purple-9')
        else:
            ui.notify("We could not receive your message. Please try again later.", type="negative")

async def contact_message_received(first_name, last_name, email_address, message_summary):
    email_sender = 'uwspsupportemailhere'
    email_password = os.environ.get('EMAIL_PASS')
    email_receiver = 'supportemailhere'
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
                        From: {first_name} {last_name}
                    </p>
                    <p>
                        Email: {email_address}
                    </p>
                    <p>
                        Message: {message_summary}
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


