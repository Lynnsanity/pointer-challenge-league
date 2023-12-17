from nicegui import app, ui

from header_footer import header_footer

@ui.page('/contact')
async def contact():
    header_footer()

    #ui.query('body').style('background-color: #181818')
    ui.query('body').classes('bg-gradient-to-t from-zinc-950 to-white-500')
