from nicegui import app, ui
from components.logic import Enable
from components.header_footer import header_footer
from contact.validator import contact_submit_click

@ui.page('/contact')
async def contact_page():

    header_footer()
    enable = Enable()
    ui.query('body').style('background-color: #181818')
    ui.query('.nicegui-content').classes('p-0')
    with ui.image('img/ow2/sombra.jpg').classes('w-full h-[800px]'):
        with ui.column().classes('w-full h-[800px] md:w-1/2 xl:w-1/2'):
            with ui.card().props('flat unelevated').classes('w-full h-full bg-transparent flex items-center text-center text-white'):
                ui.label('Contact Us').classes('font-mono text-[#ffc82e] text-3xl pt-5')
                ui.label('Have questions, comments, concerns and/or feedback?').classes('mt-5 font-mono text-xl')
                ui.label('Feel free to send us a message').classes('font-mono text-xl')
                first_name = ui.input('First Name', on_change=enable.contact_on_change,
                                      validation={"Required field":enable.empty, "Character Limit Exceeded":enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full mt-5')
                last_name = ui.input('Last Name', on_change=enable.contact_on_change, \
                                     validation={"Required field": enable.empty, "Character Limit Exceeded":enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                email_address = ui.input('Email Address', on_change=enable.contact_on_change, \
                                         validation={"Required field": enable.empty, "Invalid Email Address":enable.is_valid_email,
                                                     "Character Limit Exceeded":enable.char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                message_summary = ui.textarea('Message Summary', on_change=enable.contact_on_change, \
                                                      validation={"Required field": enable.empty, "Too many characters, max is 512": enable.message_char_limit}) \
                    .props('outlined v-model="text" color=amber dark') \
                    .classes('w-full')
                #contact_button = ui.button('Submit').props('color=amber text-color=black').classes('text-lg')
                #contact_button.bind_enabled_from(enable, "no_errors")
                contact_button = ui.button('Submit', on_click=lambda: contact_submit_click(first_name.value.strip(), last_name.value.strip(), email_address.value.strip(), message_summary.value.strip())).props('color=amber text-color=black').classes('text-lg')
                contact_button.bind_enabled_from(enable, "no_errors")
