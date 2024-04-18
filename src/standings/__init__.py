from nicegui import app, ui

from components.header_footer import header_footer


@ui.page('/standings')
async def standings_page():
    header_footer()
    ui.query('.nicegui-content').classes('p-0')
    ui.query('body').style('background-color: #181818')
    with ui.row().classes('w-full flex py-10 justify-center items-center text-center'):
        ui.image('img/pcl-logos/standings.png').classes('w-1/2 md:w-1/4 lg:w-1/4 xl:w-1/4')
        ui.label('Please stay tuned!').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
        ui.label('As more contestants continue to join, this page will be updated \
            with the contestants and match timings once the deadline for applications has passed.') \
            .classes('text-xl font-mono w-full flex text-white justify-center text-center')
        with ui.row().classes('mx-auto w-full h-full'):
            ui.html('<iframe src="https://challonge.com/mzkr4d27/module" width="100%" height="500" frameborder="0" scrolling="auto" allowtransparency="true"></iframe>').classes('w-full h-full')
            ui.mermaid('''
                graph BT

                  A[[TEAM 1 VS TEAM 2]]
                  B[[TEAM 3 VS TEAM 4]]
                  C[[TEAM 5 VS TEAM 6]]
                  D[[TEAM 7 VS TEAM 8]]
                  E[[TEAM 1 VS TEAM 3]]
                  F[[Team 5 VS TEAM 7]]
                  G[[PCL OW2 Champion]]

                  A --- E
                  B --- E
                  C --- F
                  D --- F
                  E --- G
                  F --- G
            ''').on('error', lambda e: print(e.args['message'])).classes('mx-auto flex items-center justify-center').style('width:100%; height:auto;')
    with ui.row().classes('w-full p-0 pb-10 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 xl:grid-cols-2'):
        # contestants
        with ui.column().classes('mx-auto w-full flex items-center justify-center'):
            ui.image('img/pcl-logos/contestants.png').classes('w-1/3')
            # contestant 1
            with ui.column().classes('w-full border-2 border-[#512698] p-5'):
                ui.label('team 1').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
            # contestant 2
            with ui.column().classes('w-full border-2 border-[#ffc82e] p-5'):
                ui.label('team 2').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
            # contestant 3
            with ui.column().classes('w-full border-2 border-[#512698] p-5'):
                ui.label('team 3').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
            # contestant 4
            with ui.column().classes('w-full border-2 border-[#ffc82e] p-5'):
                ui.label('team 4').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
            # contestant 5
            with ui.column().classes('w-full border-2 border-[#512698] p-5'):
                ui.label('team 5').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
            # contestant 6
            with ui.column().classes('w-full border-2 border-[#ffc82e] p-5'):
                ui.label('team 6').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
            # contestant 7
            with ui.column().classes('w-full border-2 border-[#512698] p-5'):
                ui.label('team 7').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
            # contestant 8
            with ui.column().classes('w-full border-2 border-[#ffc82e] p-5'):
                ui.label('team 8').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
        # 2024 pcl champion
        with ui.column().classes('mx-auto w-full flex items-center justify-center'):
            ui.image('img/pcl-logos/pcl-2024-champ.png').classes('w-1/2')
            with ui.column().classes('w-full p-5'):
                ui.label('1st Place: Team 1').classes('w-full text-3xl flex justify-center font-mono text-white')
                ui.label('2nd Place: Team 2').classes('w-full text-3xl flex justify-center font-mono text-white')
                ui.label('3rd Place: Team 3').classes('w-full text-3xl flex justify-center font-mono text-white')
