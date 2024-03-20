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

    with ui.row().classes('w-full bg-gradient-to-r from-yellow-500 to-purple-500 p-1'):
        ui.image('img/ow2/ramm.webp')
    #with ui.row().classes('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 mx-auto w-full h-2/3 flex items-center justify-center my-5'):
    #    ui.label('Some text here')
    #    ui.image('img/ow2/home/winston.png').classes('w-auto')

    with ui.row().classes('mx-auto my-5 text-center'):
        ui.label('GETTING STARTED').classes('text-5xl min-[320px]:text-4xl font-extrabold text-[#FFC82e] font-mono')

    with ui.row().classes('grid grid-cols-1 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-3 my-5 w-full'):
        with ui.card().tight().classes('no-shadow aspect-square bg-transparent'):
            ui.button(icon='gavel').props('flat color=white').classes('mx-auto w-full text-6xl text-center')
            #ui.image('img/games/league.png').classes('object-cover')
        with ui.card().tight().classes('no-shadow aspect-square bg-transparent'):
            ui.button(icon='sports_esports').props('flat color=white').classes('mx-auto w-full text-6xl text-center')
        with ui.card().tight().classes('no-shadow aspect-square bg-transparent'):
            ui.button(icon='feed').props('flat color=white').classes('mx-auto w-full text-6xl text-center')
            ui.label('Example').classes('w-full text-center')

    with ui.row().classes('mx-auto my-5 text-center'):
        ui.label('GAMES WE PLAY').classes('text-5xl min-[320px]:text-4xl font-extrabold text-[#FFC82e] font-mono')


    with ui.row().classes('grid grid-cols-1 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-3 w-full justify-center items-center text-center'):
        
            with ui.image('img/games/overwatch.jpg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#512698] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.label('Overwatch 2') \
                        .classes('w-full text-3xl font-mono font-bold text-black')

            with ui.image('img/games/fortnite.jpeg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#ffc82e] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.label('Fortnite').classes('w-full text-3xl font-mono font-bold text-black')

            with ui.image('img/games/league.png') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#512698] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.label('League of Legends').classes('w-full text-3xl font-mono font-bold text-black')

            with ui.image('img/games/smashbros.jpeg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#512698] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.label('Super Smash Bros.').classes('w-full text-3xl font-mono font-bold text-black')

            with ui.image('img/games/apex.jpeg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#ffc82e] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.label('Apex Legends').classes('w-full text-3xl font-mono font-bold text-black')

            with ui.image('img/games/rocketleague.jpeg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#512698] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.image('img/games/rocketleaguelogo.webp').classes('w-full')

    with ui.row().classes('mx-auto my-5 text-center'):
        ui.label('CONTACT US').classes('text-5xl min-[320px]:text-4xl font-extrabold text-[#FFC82e] font-mono')




    #ui.query('body').classes('bg-gradient-to-t from-[#512698] to-[#FFC82e]')

    #ui.query('body').classes('bg-gradient-to-t from-zinc-950 to-white-500')
