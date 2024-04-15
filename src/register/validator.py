from nicegui import ui
from components.logic import Enable
from email.message import EmailMessage
from components.sender import send_email

import os
import ssl
import smtplib

async def registration_submit_click(
    team_name,
    captain_firstname,
    captain_lastname,
    captain_ign,
    playertwo_firstname,
    playertwo_lastname,
    playertwo_ign,
    playerthree_firstname,
    playerthree_lastname,
    playerthree_ign,
    playerfour_firstname,
    playerfour_lastname,
    playerfour_ign,
    playerfive_firstname,
    playerfive_lastname,
    playerfive_ign,
    email_address,
    phone_number,
    #school_name,
    #team_logo=None,
    #subone_firstname=None,
    #subone_lastname=None,
    #subone_ign=None,
    #subtwo_firstname=None,
    #subtwo_lastname=None,
    #subtwo_ign=None
):
    enable = Enable()
    # Validate each input individually
    # Check if none of the fields are completed
    mandatory_list = [team_name,
                      captain_firstname,
                      captain_lastname,
                      captain_ign,
                      playertwo_firstname,
                      playertwo_lastname,
                      playertwo_ign,
                      playerthree_firstname,
                      playerthree_lastname,
                      playerthree_ign,
                      playerfour_firstname,
                      playerfour_lastname,
                      playerfour_ign,
                      playerfive_firstname,
                      playerfive_lastname,
                      playerfive_ign,
                      email_address,
                      phone_number]

    fields = {
        "captain_firstname": ("captain first name", captain_firstname),
        "captain_lastname": ("captain last name", captain_lastname),
        "captain_ign": ("captain in game name", captain_ign),
        "playertwo_firstname": ("player two first name", playertwo_firstname),
        "playertwo_lastname": ("player two last name", playertwo_lastname),
        "playertwo_ign": ("player two in game name", playertwo_ign),
        "playerthree_firstname": ("player three first name", playerthree_firstname),
        "playerthree_lastname": ("player three last name", playerthree_lastname),
        "playerthree_ign": ("player three in game name", playerthree_ign),
        "playerfour_firstname": ("player fourfirst name", playerfour_firstname),
        "playerfour_lastname": ("player four last name", playerfour_lastname),
        "playerfour_ign": ("player four in game name", playerfour_ign),
        "playerfive_firstname": ("captain first name", playerfive_firstname),
        "playerfive_lastname": ("captain last name", playerfive_lastname),
        "playerfive_ign": ("captain in game name", playerfive_ign),
        "email_address": ("email address", email_address),
        "phone_number": ("phone number", phone_number)
    }
    errors = []

    for field, (label, value) in fields.items():
        if not enable.empty(value):
            errors.append(f"Please enter your {label}.")
        elif not enable.char_limit(value):
            errors.append(f"There are too many characters in {label}.")
        elif field == "email_address" and not enable.is_valid_email(value):
            errors.append("Please enter a valid email address.")
        elif field == "phone_number" and not enable.is_valid_phone_number(value):
            errors.append("Please enter a valid phone number.")

    if errors:
        for error in errors:
            ui.notify(error, type="error")
    else:

        email_sent = await registration_application_received(
            team_name=team_name,
            captain_firstname=captain_firstname,
            captain_lastname=captain_lastname,
            captain_ign=captain_ign,
            playertwo_firstname=playertwo_firstname,
            playertwo_lastname=playertwo_lastname,
            playertwo_ign=playertwo_ign,
            playerthree_firstname=playerthree_firstname,
            playerthree_lastname=playerthree_lastname,
            playerthree_ign=playerthree_ign,
            playerfour_firstname=playerfour_firstname,
            playerfour_lastname=playerfour_lastname,
            playerfour_ign=playerfour_ign,
            playerfive_firstname=playerfive_firstname,
            playerfive_lastname=playerfive_lastname,
            playerfive_ign=playerfive_ign,
            email_address=email_address,
            phone_number=phone_number)

        if email_sent:
            receipt = await send_confirmation(
                team_name=team_name,
                captain_firstname=captain_firstname,
                captain_lastname=captain_lastname,
                captain_ign=captain_ign,
                playertwo_firstname=playertwo_firstname,
                playertwo_lastname=playertwo_lastname,
                playertwo_ign=playertwo_ign,
                playerthree_firstname=playerthree_firstname,
                playerthree_lastname=playerthree_lastname,
                playerthree_ign=playerthree_ign,
                playerfour_firstname=playerfour_firstname,
                playerfour_lastname=playerfour_lastname,
                playerfour_ign=playerfour_ign,
                playerfive_firstname=playerfive_firstname,
                playerfive_lastname=playerfive_lastname,
                playerfive_ign=playerfive_ign,
                email_address=email_address,
                phone_number=phone_number)
            if receipt:
                ui.notify(f"Thank you! "
                          f"Successfully sent application and receipt to {email_address} ."
                          f"Please keep checking your email for further updates soon. ",
                          type='positive',
                          color='purple-9',
                          multi_line=True,
                          classes='multi-line-notification')
            else:
                ui.notify(f"Thank you! "
                          f"Successfully sent application. Failed to send receipt to {email_address}. "
                          f"If you need your receipt, please contact support. "
                          f"Otherwise, please keep checking your email for further updates soon.",
                          type='positive',
                          color='purple-9',
                          multi_line=True,
                          classes='multi-line-notification')
        else:
            ui.notify(f"We could not receive your application. "
                      f"We are experiencing technical difficulties, "
                      f"please try again later.",
                      type="negative",
                      multi_line=True,
                      classes='multi-line-notification')

async def registration_application_received(
            team_name,
            captain_firstname,
            captain_lastname,
            captain_ign,
            playertwo_firstname,
            playertwo_lastname,
            playertwo_ign,
            playerthree_firstname,
            playerthree_lastname,
            playerthree_ign,
            playerfour_firstname,
            playerfour_lastname,
            playerfour_ign,
            playerfive_firstname,
            playerfive_lastname,
            playerfive_ign,
            email_address,
            phone_number
):
    email_sender = 'uwspdummyemailiguess'
    email_password = os.environ.get('EMAIL_PASS')
    email_receiver = "uwspregistrationemailhere"
    registration_deadline = "07/01/2024"
    subject = 'Registration Received'
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
                    <h2>Overwatch 2 PCL 2024 Competition Application Details.</h2>
                    <p>
                    Application Details:<br>
                    Team Name: {team_name}<br>
                    Captain Name: {captain_firstname} {captain_lastname}<br>
                    Captain IGN: {captain_ign}<br>
                    Player 2 Name: {playertwo_firstname} {playertwo_lastname}<br>
                    Player 2 IGN: {playertwo_ign}<br>
                    Player 3 Name: {playerthree_firstname} {playerthree_lastname}<br>
                    Player 3 IGN: {playerthree_ign}<br>
                    Player 4 Name: {playerfour_firstname} {playerfour_lastname}<br>
                    Player 4 IGN: {playerfour_ign}<br>
                    Player 5 Name: {playerfive_firstname} {playerfive_lastname}<br>
                    Player 5 IGN: {playerfive_ign}<br>
                    Submittee Contact Details:<br>
                    Email Address: {email_address}<br>
                    Phone Number: {phone_number}<br>
                    </p>
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

async def send_confirmation(
            team_name,
            captain_firstname,
            captain_lastname,
            captain_ign,
            playertwo_firstname,
            playertwo_lastname,
            playertwo_ign,
            playerthree_firstname,
            playerthree_lastname,
            playerthree_ign,
            playerfour_firstname,
            playerfour_lastname,
            playerfour_ign,
            playerfive_firstname,
            playerfive_lastname,
            playerfive_ign,
            email_address,
            phone_number
):
    email_sender = 'auwspemailiguess@gmail.com'
    email_password = os.environ.get('EMAIL_PASS')
    email_receiver = email_address
    registration_deadline = "07/01/2024"

    subject = 'Registration Application Receipt'
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
                        with information regarding the match details.
                    </p>
                    <br>
                    <p>
                        Any changes to the application MUST be submitted through support contact
                        before the registration deadline {registration_deadline}.
                        Changes made after the deadline will NOT be considered.
                        Please make sure to submit any changes before the deadline.
                    </p>
                    <br>
                    <p>
                    Application Details:<br>
                    Team Name: {team_name}<br>
                    Captain Name: {captain_firstname} {captain_lastname}<br>
                    Captain IGN: {captain_ign}<br>
                    Player 2 Name: {playertwo_firstname} {playertwo_lastname}<br>
                    Player 2 IGN: {playertwo_ign}<br>
                    Player 3 Name: {playerthree_firstname} {playerthree_lastname}<br>
                    Player 3 IGN: {playerthree_ign}<br>
                    Player 4 Name: {playerfour_firstname} {playerfour_lastname}<br>
                    Player 4 IGN: {playerfour_ign}<br>
                    Player 5 Name: {playerfive_firstname} {playerfive_lastname}<br>
                    Player 5 IGN: {playerfive_ign}<br>
                    Submittee Contact Details:<br>
                    Email Address: {email_address}<br>
                    Phone Number: {phone_number}<br>
                    </p>
                    <p>
                    Sincerely,<br>
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
