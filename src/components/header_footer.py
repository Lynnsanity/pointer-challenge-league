from nicegui import app,ui


def header_footer():
    with ui.header(elevated=True).style('background-color: #181818').classes('items-center justify-between fixed'):
        with ui.link('', '/home'):
            ui.image('./img/pcl-logos/glow-pcl.png').classes('w-[270px]')
        with ui.row().classes('max-sm:hidden font-mono'):
            ui.button('Rules', icon='gavel', on_click=lambda: ui.open('/rules')).props('flat color=white')
            ui.button('Register', icon='feed', on_click=lambda: ui.open('/register')).props('flat color=white')
            ui.button('Standings', icon='emoji_events', on_click=lambda: ui.open('/standings')).props('flat color=white')
            ui.button('Contact', icon='contact_support', on_click=lambda: ui.open('/contact')).props('flat color=white')
        with ui.row().classes('sm:hidden'):
            with ui.button(icon='menu').props('flat color=white'):
                with ui.menu().style('background-color: #181818').classes('text-white border-2 border-purple-500 border-opacity-50 font-mono') as menu:
                    ui.menu_item('Rules', on_click=lambda: ui.open('/rules')).classes('px-5 py-3 flex justify-center text-center')
                    ui.menu_item('Register', on_click=lambda: ui.open('/register')).classes('px-5 py-3flex justify-center text-center')
                    ui.menu_item('Standings', on_click=lambda: ui.open('/standings')).classes('px-5 py-3 flex justify-center text-center')
                    ui.menu_item('Contact', on_click=lambda: ui.open('/standings')).classes('px-5 py-3 flex justify-center text-center')

    with ui.footer(fixed=False).style('background-color: #181818'):
        with ui.row().classes('mx-auto w-full'):
            with ui.row().classes('grid grid-cols-2'):
                with ui.link(target='https://www.uwsp.edu/'):
                    ui.image('./img/uwsp-logos/uwsp-circle.png').classes('w-[100px]')
                    ui.image('./img/uwsp-logos/uwsp-words.png').classes('w-[200px] ml-2')
                with ui.link(target='https://www.uwsp.edu/esports/'):
                    ui.image('./img/uwsp-logos/uwsp-esports.png').classes('w-[150px] mt-2')
            #ui.label('example').classes('w-full flex items-center justify-center')

