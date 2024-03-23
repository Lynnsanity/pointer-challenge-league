from nicegui import app, ui

from nicegui import ui

class Enable:
    def __init__(self) -> None:
        self.inputs = {}
        self.no_errors = True

    def is_not_empty(self, v):
        return v and len(v) > 0

    def on_change(self, e):
        valid = self.is_not_empty(e.value)
        self.inputs[e.sender.id] = valid
        self.update()

    def update(self):
        for i in self.inputs.values():
            if i is not True:
                self.no_errors = False
                break
        else:
            self.no_errors = True

async def submit_registration():
    ui.notify('it gets this far')

def form():
    enable = Enable()
    with ui.column().classes('flex items-center justify-center text-center \
                             w-full md:w-3/4 lg:w-1/2 xl:w-1/2 2xl:w-1/2 mt-10 font-mono'):

        ui.label('Team Information').classes('w-full flex text-start text-lg text-[#ffc82e]')
        # team name
        team_name = ui.input('Team Name *', on_change=enable.on_change, validation={"Required field": enable.is_not_empty}) \
            .props('outlined v-model="text" color=amber') \
            .classes('w-full')

        # optional affiliated school
        with ui.input('University / College Name') \
            .props('outlined v-model="text" color=amber') \
                .classes('w-full mt-5') as school_name:
            ui.tooltip('Optional: If your team is officially affiliated with a Uni / College, enter the \
                       school name here') .classes('bg-purple')

        ui.label('Team Logo').classes('w-full flex text-start text-lg text-[#ffc82e] mt-5')
        team_logo = ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}'),
              on_rejected=lambda: ui.notify('File size too big. Maximum size is 500KB'),
              max_file_size=500_000).classes('max-w-full')


        # tourney requirements
        with ui.column() \
                .classes('w-full flex text-start'):
            ui.label('Tournament Requirements').classes('mt-5')
            ui.markdown('- Each team **MUST** have **5 players** and **MAY** have up to **2 substitutes**.')
            ui.label("Please provide each team member's information below.")

        with ui.column().classes('w-full flex text-start text-lg'):
            # captain (player 1)
            ui.label('Captain').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                captain_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                captain_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
            captain_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber') \
                .classes('w-full')

            # player 2
            ui.label('Player #2').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playertwo_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                playertwo_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
            playertwo_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber') \
                .classes('w-full')

            # player 3
            ui.label('Player #3').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerthree_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                playerthree_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
            playerthree_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber') \
                .classes('w-full')

            # player 4
            ui.label('Player #4').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerfour_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                playerfour_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
            playerfour_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber') \
                .classes('w-full')

            # player 5
            ui.label('Player #5').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerfive_firstname = ui.input('First Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                playerfive_lastname = ui.input('Last Name *') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
            playerfive_ign = ui.input('In Game Name *') \
                .props('outlined v-model="text" color=amber') \
                .classes('w-full')

            # substitute #1
            ui.label('Substitute #1').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                subone_firstname = ui.input('First Name') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                subone_lastname = ui.input('Last Name') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
            subone_ign = ui.input('In Game Name') \
                .props('outlined v-model="text" color=amber') \
                .classes('w-full')

            # substitute #2
            ui.label('Substitute #2').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                subtwo_firstname = ui.input('First Name') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                subtwo_lastname = ui.input('Last Name') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
            subtwo_ign = ui.input('In Game Name') \
                .props('outlined v-model="text" color=amber') \
                .classes('w-full')

        ui.label('Contact Information').classes('w-full flex text-start text-lg text-[#ffc82e]')
        # team name
        email_address = ui.input('Email Address *') \
            .props('outlined v-model="email" color=amber') \
            .classes('w-full')
        phone_number = ui.input('Phone Number *') \
            .props('outlined v-model="tel" color=amber') \
            .classes('w-full')

        # agree to rules
        agree_checkbox = ui.checkbox('By selecting this checkbox, you and your team acknowledge \
        that you all have read and agree to abide by the rules outlined on the Rules page.') \
            .classes('text-bold')

        #register_button = ui.button('Submit Registration', on_click=lambda: submit_registration() if enable.no_errors else None)

        register_button = ui.button('Submit Registration', on_click=submit_registration)
        register_button.bind_enabled_from(enable, "no_errors")


