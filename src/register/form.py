import re
from nicegui import app, ui, events
from email_validator import validate_email, EmailNotValidError


class Enable:
    def __init__(self) -> None:
        self.inputs = {}
        self.no_errors = True

    def is_not_empty(self, v):
        return v and len(v) > 0

    def is_valid_email(self, email):
      try:
        email_info = validate_email(email, check_deliverability=False)
        email = email_info.normalized
        return True
      except EmailNotValidError as e:
        print(f"Email validation error: {e}")
        return False


    def is_valid_phone_number(self, phone_number):
        try:
            phone_number = ''.join(c for c in phone_number if c.isdigit())
            if len(phone_number) != 10:
                return False
            return True
        except EmailNotValidError as e:
            print(f"Email validation error: {e}")
            return False

    def on_change(self, e):
        field_id = e.sender.id
        if field_id == "email_address":
            result = self.is_valid_email(e.value)
            if not self.is_not_empty(e.value):
                e.sender.set_validation_message("Required field")
            elif not result:
                e.sender.set_validation_message("Please enter a valid email.")
            else:
                e.sender.clear_validation_message()
        else:
            valid = self.is_not_empty(e.value)
            self.inputs[field_id] = valid
            self.update()

    def update(self):
        for i in self.inputs.values():
            if i is not True:
                self.no_errors = False
                break
        else:
            self.no_errors = True

class Logic:
    def __init__(self):
        self.selected_value = 0
        self.subone_firstname = ui.input('First Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subone_lastname = ui.input('Last Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subone_ign = ui.input('In Game Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subone_firstname.visible = False
        self.subone_lastname.visible = False
        self.subone_ign.visible = False
        self.subtwo_firstname = ui.input('First Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subtwo_lastname = ui.input('Last Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subtwo_ign = ui.input('In Game Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subtwo_firstname.visible = False
        self.subtwo_lastname.visible = False
        self.subtwo_ign.visible = False

    def update_visibility(self, e: events.ValueChangeEventArguments):
        self.selected_value = e.value
        self.update_inputs()

    def update_inputs(self):
        # clear all inputs
        self.subone_firstname.visible = False
        self.subone_lastname.visible = False
        self.subone_ign.visible = False
        self.subtwo_firstname.visible = False
        self.subtwo_lastname.visible = False
        self.subtwo_ign.visible = False
        
        # shows input 1 if 1 or 2 is selected
        if self.selected_value >= 1:
            self.subone_firstname.visible = True
            self.subone_lastname.visible = True
            self.subone_ign.visible = True

        # shows input2 if 2 is selected
        if self.selected_value == 2:
            self.subtwo_firstname.visible = True
            self.subtwo_lastname.visible = True
            self.subtwo_ign.visible = True

async def submit_registration():
    ui.notify('it gets this far')

def form():
    enable = Enable()
    with ui.column().classes('flex items-center justify-center text-center \
                             w-full md:w-3/4 lg:w-1/2 xl:w-1/2 2xl:w-1/2 mt-10 font-mono'):

        ui.label('Team Information').classes('w-full flex text-start text-lg text-[#ffc82e]')

        # team name
        team_name = ui.input('Team Name *', on_change=enable.on_change, \
                             validation={"Required field": enable.is_not_empty}) \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')


        # optional affiliated school
        with ui.input('University / College Name') \
            .props('outlined v-model="text" color=amber dark') \
                .classes('w-full mt-5') as school_name:
            ui.tooltip('Optional: If your team is officially affiliated with a Uni / College, enter the \
                       school name here') .classes('bg-purple')

        ui.label('Team Logo').classes('w-full flex text-start text-lg text-[#ffc82e] mt-5')
        team_logo = ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}'),
              on_rejected=lambda: ui.notify('File size too big. Maximum size is 500KB'),
              max_file_size=500_000).classes('max-w-full').props('color=purple-9 dark') \
            .classes('w-full text-start')


        # tourney requirements
        with ui.column() \
                .classes('w-full flex text-start text-white'):
            ui.label('Tournament Requirements').classes('mt-5')
            ui.markdown('- Each team **MUST** have **5 players** and **MAY** have up to **2 substitutes**.')

        with ui.column().classes('w-full flex text-start text-lg'):
            # player(s) information
            ui.label('Player Information').classes('w-full flex text-start text-lg text-[#ffc82e]')
            # captain (player 1)
            ui.label('Captain').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                captain_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                captain_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            captain_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # player 2
            ui.label('Player #2').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playertwo_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                playertwo_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            playertwo_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # player 3
            ui.label('Player #3').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerthree_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                playerthree_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            playerthree_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # player 4
            ui.label('Player #4').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerfour_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                playerfour_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            playerfour_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # player 5
            ui.label('Player #5').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerfive_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                playerfive_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            playerfive_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # sub information
            ui.label('Substitute Player Information').classes('w-full flex text-start text-lg text-[#ffc82e]')
            logic = Logic()
            with ui.row().classes('w-full flex text-start text-sm text-white'):
                    ui.markdown('How many substitutes?')
                    ui.radio([0, 1, 2], value=0, on_change=logic.update_visibility) \
                        .props('dark color=purple-9')


        ui.label('Contact Information').classes('w-full flex text-start text-lg text-[#ffc82e]')
        
        # contact info
        email_address = ui.input('Email Address *', on_change=enable.on_change, \
                                 validation={"Required field": enable.is_not_empty, "Invalid Email": enable.is_valid_email}) \
            .props('outlined v-model="email" color=amber dark') \
            .classes('w-full')
        phone_number = ui.input('Phone Number *', on_change=enable.on_change, \
                                validation={"Required field": enable.is_not_empty, "Invalid Phone Number": enable.is_valid_phone_number}) \
            .props('outlined v-model="tel" color=amber dark') \
            .classes('w-full')

        # agree to rules
        agree_checkbox = ui.checkbox('By selecting this checkbox, you and your team acknowledge \
        that you all have read and agree to abide by the rules outlined on the Rules page.') \
            .classes('text-bold text-white text-start justify-left') \
            .props('dark')

        #register_button = ui.button('Submit Registration', on_click=lambda: submit_registration() if enable.no_errors else None)

        register_button = ui.button('Submit Registration', on_click=submit_registration)
        register_button.bind_enabled_from(enable, "no_errors")


