from nicegui import app, ui

from components.header_footer import header_footer

from home.carousel import carousel
from rules import rules_page

@ui.page('/home')
async def home_page():
    header_footer()

    ui.query('.nicegui-content').classes('p-0')
    ui.query('body').style('background-color: #181818')
    carousel()

    with ui.row().classes('w-full bg-gradient-to-r from-yellow-500 to-purple-500 p-1'):
        ui.image('img/ow2/ram2.jpg')

    with ui.row().classes('w-full'):
        ui.image('img/pcl-logos/getting-started.png').classes('mx-auto w-3/4 md:w-1/2 lg:w-1/3 xl:w-1/3 my-5 flex justify-center')

    with ui.row().classes('w-full h-full flex grid grid-cols-1 px-10 gap-10 md:grid-cols-3 lg:grid-cols-3 my-5 w-full'):
        with ui.link(target='/rules').classes('no-underline'):
            with ui.card().tight().classes('w-full h-full no-shadow aspect-square bg-[#512698]'):
                ui.icon('gavel').props('flat color=white').classes('mx-auto w-full mt-10 text-9xl text-center')
                ui.image('img/pcl-logos/rules.png').classes('mx-auto my-5 w-1/3 flex justify-center')
                with ui.column().classes('w-full h-[330px] p-5'):
                    ui.label('Fair play is at the core of our community. '
                             'Before you dive into the action, take a moment to familiarize yourself '
                             'with our rules. Click here to explore further details. ') \
                        .classes('text-lg sm:md:text-sm md:text-md lg:text-lg xl:text-lg 2xl:text-3xl text-[#ffc82e] px-5 font-mono font-bold')
        with ui.link(target='/register').classes('no-underline'):
            with ui.card().tight().classes('w-full h-full no-shadow aspect-square bg-[#FFC82E]'):
                ui.icon('feed').props('flat color=white').classes('mx-auto w-full mt-10 text-9xl text-center')
                ui.image('img/pcl-logos/register-purple.png').classes('mx-auto my-5 w-1/2 flex justify-center')
                with ui.column().classes('w-full h-[330px] p-5'):
                    ui.label("Already understand the rules? Great! "
                             "Take the next step by clicking here to fill "
                             "out the application for your team's gaming sessions. "
                             "Let's get you in the game – register now! ") \
                        .classes('text-lg sm:md:text-sm md:text-md lg:text-lg xl:text-lg 2xl:text-3xl text-[#512698] px-5 font-mono font-bold')
        with ui.link(target='/standings').classes('no-underline'):
            with ui.card().tight().classes('w-full h-full no-shadow aspect-square bg-[#512698]'):
                ui.icon('emoji_events').props('flat color=white').classes('mx-auto w-full mt-10 text-9xl text-center')
                ui.image('img/pcl-logos/standings.png').classes('mx-auto my-5 w-3/5 flex justify-center')
                with ui.column().classes('w-full h-[330px] p-5'):
                    ui.label("Curious about where your team stands? Click here to view "
                             "the latest standings and see how you stack up against the "
                             "competition. Keep track of your progress and aim for the top spot!") \
                        .classes('text-lg sm:md:text-sm md:text-md lg:text-lg xl:text-lg 2xl:text-3xl text-[#ffc82e] px-5 font-mono font-bold')

    with ui.row().classes('w-full'):
        ui.image('img/pcl-logos/games-we-play.png').classes('mx-auto w-3/4 md:w-1/2 lg:w-1/3 xl:w-1/3 my-5 flex justify-center')


    with ui.row().classes('grid grid-cols-2 sm:grid-cols-3 md:grid-cols-3 lg:grid-cols-3 w-full mb-10 justify-center items-center text-center'):
            with ui.image('img/games/overwatch.jpg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#ffc82e] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.image('img/ow2/ow2logo2.png').classes('w-full')

            with ui.image('img/games/fortnite.jpeg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#512698] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.image('img/games/fortnitelogo.png').classes('w-full')

            with ui.image('img/games/league.png') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#ffc82e] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.image('img/games/lollogo2.png').classes('w-full')

            with ui.image('img/games/smashbros.jpeg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#512698] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.image('img/games/ssbu-logo.png').classes('w-full')

            with ui.image('img/games/apex.jpeg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#ffc82e] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.image('img/games/apexlegendslogo2.png').classes('w-full')

            with ui.image('img/games/rocketleague.jpeg') \
                    .classes('mx-auto transition-all duration-500 ease-in-out hover:scale-105 rounded-lg \
                             aspect-square w-4/5 no-shadow bg-transparent border-[#512698] border-2 mt-5'):
                with ui.card() \
                        .props('flat unelevated') \
                        .classes('w-full h-full opacity-0 hover:opacity-100 flex justify-center items-center text-center'):
                    ui.image('img/games/rocketleaguelogo.webp').classes('w-full')

    with ui.row().classes('mx-auto w-full bg-[#512698] p-5 flex items-center justify-center'):
        ui.image('img/pcl-logos/questions-feedback-concerns.png').classes('w-full md:w-1/2 lg:w-1/2 xl:w-1/2')
        ui.button('Contact Us').props('color=amber text-color=black')
