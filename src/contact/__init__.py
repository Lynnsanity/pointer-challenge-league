from nicegui import app, ui

from components.header_footer import header_footer

@ui.page('/contact')
async def contact_page():
    header_footer()
    
    
    # background color of page
    ui.query('body').style('background-color: #181818')
    #ui.query('body').classes('bg-gradient-to-t from-zinc-950 to-white-500')


    with ui.image('img/ow2/tracer.jpg').classes('w-full h-full'):
        with ui.row().classes('w-full h-full'):
            with ui.card().props('flat unelevated').classes('w-1/2 h-full bg-transparent flex items-center text-center'):
                ui.label('Contact Us').classes('font-mono text-[#ffc82e] text-3xl')
                ui.label('Have questions, comments, concerns and/or feedback?').classes('mt-5 font-mono text-[#ffc82e] text-black text-xl')
                ui.label('Feel free to send us a message').classes('font-mono text-[#ffc82e] text-black text-xl')
        
                # optional affiliated school
                contact_team_name = ui.input('Team Name') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full mt-5')
                contact_message_title = ui.input('Message Title') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                contact_message_summary = ui.input('Message Summary') \
                    .props('outlined v-model="text" color=amber') \
                    .classes('w-full')
                ui.button('Submit').props('color=black').classes('text-lg')
