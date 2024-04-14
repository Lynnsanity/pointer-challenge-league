from nicegui import app, ui, events
from components.logic import Enable
from register.validator import registration_submit_click
from register.sub_logic import Logic


def form():
    enable = Enable()
    with ui.column().classes('flex items-center justify-center text-center \
                             w-full md:w-3/4 lg:w-1/2 xl:w-1/2 2xl:w-1/2 mt-10 font-mono'):

        ui.label('Team Information').classes('w-full flex text-start text-lg text-[#ffc82e]')

        # team name
        team_name = ui.input('Team Name *', on_change=enable.registration_on_change, \
                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        # optional affiliated school
        with ui.input('University / College Name', on_change=enable.registration_on_change,
                      validation={"Character Limit Exceeded": enable.char_limit}) \
            .props('outlined v-model="text" color=amber dark') \
                .classes('w-full mt-5') as school_name:
            ui.tooltip('Optional: If your team is officially affiliated with a Uni / College, enter the \
                       school name here').classes('bg-purple')

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
                captain_firstname = ui.input('First Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                captain_lastname = ui.input('Last Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            captain_ign = ui.input('In Game Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # player 2
            ui.label('Player #2').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playertwo_firstname = ui.input('First Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                playertwo_lastname = ui.input('Last Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            playertwo_ign = ui.input('In Game Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # player 3
            ui.label('Player #3').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerthree_firstname = ui.input('First Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                playerthree_lastname = ui.input('Last Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            playerthree_ign = ui.input('In Game Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # player 4
            ui.label('Player #4').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerfour_firstname = ui.input('First Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                playerfour_lastname = ui.input('Last Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            playerfour_ign = ui.input('In Game Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # player 5
            ui.label('Player #5').classes('text-[#ffc82e]')
            with ui.row().classes('w-full grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2 2xl:grid-cols-2'):
                playerfive_firstname = ui.input('First Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                playerfive_lastname = ui.input('Last Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
            playerfive_ign = ui.input('In Game Name *', on_change=enable.registration_on_change,
                                             validation={"Required Field": enable.empty, "Character Limit Exceeded": enable.char_limit}) \
                .props('outlined v-model="text" color=amber dark') \
                .classes('w-full')

            # sub information
            ui.label('Substitute Player Information').classes('w-full flex text-start text-lg text-[#ffc82e]')
            logic = Logic()
            with ui.row().classes('w-full flex text-start text-sm text-white'):
                    ui.markdown('How many substitutes?')
                    ui.radio([0, 1, 2], value=0, on_change=logic.update_visibility) \
                        .props('dark color=purple-9 inline')
            subone_firstname = logic.subone_firstname
            subone_lastname = logic.subone_lastname
            subone_ign = logic.subone_ign
            subtwo_firstname = logic.subtwo_firstname
            subtwo_lastname = logic.subtwo_lastname
            subtwo_ign = logic.subtwo_ign

        ui.label('Contact Information').classes('w-full flex text-start text-lg text-[#ffc82e]')
        
        # contact info
        email_address = ui.input('Email Address *', on_change=enable.registration_on_change, \
                                 validation={"Required field": enable.empty, "Invalid Email": enable.is_valid_email, "Character Limit Exceeded": enable.char_limit}) \
            .props('outlined v-model="email" color=amber dark') \
            .classes('w-full')
        phone_number = ui.input('Phone Number *', on_change=enable.registration_on_change, \
                                validation={"Required field": enable.empty, "Invalid Phone Number": enable.is_valid_phone_number}) \
            .props('outlined v-model="tel" color=amber dark') \
            .classes('w-full')

        # agree to rules
        agree_checkbox = ui.checkbox('By selecting this checkbox, you and your team acknowledge \
        that you all have read and agree to abide by the rules stated on the Rules page.') \
            .classes('text-bold text-white text-start justify-left') \
            .props('dark')

        #register_button = ui.button('Submit Registration', on_click=lambda: submit_registration(teamy=teeeam) if enable.no_errors else None)
        #register_button = ui.button('submit registration', on_click=lambda e:submit_registration_um(teamy=teeeam)) \
        #    .props('color=amber text-color=black')
        #register_button.bind_enabled_from(enable, "no_errors")
        spinner = ui.spinner(size='xl').props('color=amber').classes('absolute-center')
        spinner.visible = False
        register_button = ui.button('Submit', on_click=lambda: registration_submit_click(
            team_name.value.strip(),
            captain_firstname.value.strip(),
            captain_lastname.value.strip(),
            captain_ign.value.strip(),
            playertwo_firstname.value.strip(),
            playertwo_lastname.value.strip(),
            playertwo_ign.value.strip(),
            playerthree_firstname.value.strip(),
            playerthree_lastname.value.strip(),
            playerthree_ign.value.strip(),
            playerfour_firstname.value.strip(),
            playerfour_lastname.value.strip(),
            playerfour_ign.value.strip(),
            playerfive_firstname.value.strip(),
            playerfive_lastname.value.strip(),
            playerfive_ign.value.strip(),
            #team_logo,
            #school_name.value.strip(),
            #subone_firstname.value.strip(),
            #subone_lastname.value.strip(),
            #subone_ign.value.strip(),
            #subtwo_firstname.value.strip(),
            #subtwo_lastname.value.strip(),
            #subtwo_ign.value.strip(),
            email_address.value.strip(),
            phone_number.value.strip())).props('color=amber text-color=black').classes('text-lg')
        register_button.bind_enabled_from(enable, "no_errors")



