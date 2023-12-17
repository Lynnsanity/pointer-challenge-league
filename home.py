from nicegui import app, ui

from header_footer import header_footer

@ui.page('/home')
async def home():
    header_footer()
    
    with ui.carousel(animated=True, arrows=True, navigation=True).props('height=700px'):
        with ui.carousel_slide().classes('p-0'):
            ui.image('./img/ow2/home/season-open.png').classes('max-w-full max-h-full')

    #ui.query('body').style('background-color: #181818')
    ui.query('body').classes('bg-gradient-to-t from-zinc-950 to-white-500')
