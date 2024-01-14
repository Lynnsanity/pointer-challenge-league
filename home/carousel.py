from nicegui import app,ui

def carousel():
    with ui.carousel(animated=True, arrows=True, navigation=True).classes('w-full sm:h-half md:h-[800px] relative bg-gradient-to-r from-purple-500 to-yellow-500 p-1'):
        with ui.carousel_slide().classes('p-0 w-full h-full ease-in-out'):
            ui.image('./img/ow2/home/openseason.jpg').classes('w-full h-full')
        with ui.carousel_slide().classes('p-0 w-full h-full ease-in-out'):
            ui.image('./img/esports/esports-room.jpg').classes('w-full h-full')

