from nicegui import app, ui

from components.header_footer import header_footer

from home.carousel import carousel
from rules import rules_page

@ui.page('/home')
async def home_page():
    header_footer()

    ui.query('body').style('background-color: #181818')
    #ui.image('./img/ow2/home/season-open.png').classes('mx-auto')
    carousel()

    with ui.row().classes('grid grid-cols-1 md:grid-cols-2 mx-auto flex items-center justify-center my-5 w-full md:w-2/3'):
        ui.label('Some text here')
        ui.image('img/ow2/home/winston.png').classes('w-auto')

    with ui.row().classes('mx-auto my-5 text-center'):
        ui.label('GETTING STARTED').classes('text-5xl min-[320px]:text-4xl font-extrabold text-[#FFC82e] font-mono')

    with ui.row().classes('grid grid-cols-3 my-5 w-full'):
        with ui.card().tight().classes('no-shadow aspect-square'):
            ui.image('img/games/league.png').classes('object-cover')
        with ui.card().tight().classes('no-shadow aspect-square border-[1px]'):
            ui.image('img/games/league.png').classes('object-cover')
        with ui.card().tight().classes('no-shadow aspect-square border-[1px]'):
            ui.image('img/games/league.png').classes('object-cover')

    with ui.row().classes('mx-auto my-5 text-center'):
        ui.label('GAMES WE PLAY').classes('text-5xl min-[320px]:text-4xl font-extrabold text-[#FFC82e] font-mono')


    with ui.row().classes('relative overflow-hidden grid min-[320px]:grid-cols-2 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-3 my-3 w-full justify-center items-center text-center'):
        with ui.row().classes('overflow-none bg-cover bg-no-repeat'):
            with ui.image('img/games/overwatch.jpg').classes('object-cover mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg hover:opacity-50 my-2 aspect-square w-3/4'):
                ui.label('Overwatch').classes('absolute w-full text-white text-5xl')
        with ui.row().classes('overflow-none bg-cover bg-no-repeat'):
            ui.image('img/games/fortnite.jpeg').classes('object-cover mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg hover:opacity-50 my-2 aspect-square w-3/4')
        with ui.row().classes('overflow-none bg-cover bg-no-repeat'):
            ui.image('img/games/league.png').classes('object-cover mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg hover:opacity-50 my-2 aspect-square w-3/4')
        with ui.row().classes('overflow-none bg-cover bg-no-repeat'):
            ui.image('img/games/smashbros.jpeg').classes('object-cover mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg hover:opacity-50 my-2 aspect-square w-3/4')
        with ui.row().classes('overflow-none bg-cover bg-no-repeat'):
            ui.image('img/games/apex.jpeg').classes('object-cover mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg hover:opacity-50 my-2 aspect-square w-3/4')
        with ui.row().classes('overflow-none bg-cover bg-no-repeat'):
            ui.image('img/games/rocketleague.jpeg').classes('object-cover mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg hover:opacity-70 my-2 aspect-square w-4/5')
            #ui.image('./img/games/rocketleaguelogo.webp').classes('absolute mx-auto object-cover w-1/5')


    #ui.query('body').classes('bg-gradient-to-t from-[#512698] to-[#FFC82e]')

    #ui.query('body').classes('bg-gradient-to-t from-zinc-950 to-white-500')
