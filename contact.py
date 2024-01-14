from nicegui import app, ui

from header_footer import header_footer

@ui.page('/contact')
async def contact():
    header_footer()
    
    # background color of page
    ui.query('body').style('background-color: #181818')
    #ui.query('body').classes('bg-gradient-to-t from-zinc-950 to-white-500')

    
    ui.label('Contact Us').classes(
        'mb-4 text-4xl font-extrabold font-mono leading-none tracking-tight text-white md:text-5xl lg:text-6xl')

