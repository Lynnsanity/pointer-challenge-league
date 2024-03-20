from nicegui import app, ui

from components.header_footer import header_footer


@ui.page('/standings')
async def standings_page():
    header_footer()
    
    ui.query('body').style('background-color: #181818')
    with ui.row().classes('flex justify-center items-center text-center'):
        ui.label('Please stay tuned!').classes('w-full text-3xl flex justify-center font-mono text-[#ffc82e]')
        ui.label('As more contestants continue to join, this page will be regularly updated \
            with the tournament brackets once *date* has passed.') \
            .classes('text-xl font-mono w-full flex justify-center text-center')
    #with ui.row().classes('mx-auto w-full h-full'):
    ui.mermaid('''
        graph LR

          A[Round 1 - Match 1]
          B[Round 1 - Match 2]
          C[Round 1 - Match 3]
          D[Round 1 - Match 4]
          E[Round 2 - Match 5]
          F[Round 2 - Match 6]
          G[Champion]

          A --- E
          B --- E
          C --- F
          D --- F
          E --- G
          F --- G
    ''').on('error', lambda e: print(e.args['message'])).classes('mx-auto flex items-center justify-center').style('width:100%; height:auto;')
    #ui.mermaid('''
    #    flowchart  TD
    #          subgraph diamond
    #          Prize[A: PCL TEAM CHAMPION]
    #          subgraph silver
    #            Prize --- B[Team B]
    #            Prize --- C[Team C]
    #            B --- B1[Team B]
    #            B --- B2[Another team]
    #            C --- C1[Team C]
    #            C --- C2[Another team]
    #            end
    #''').on('error', lambda e: print(e.args['message'])).classes('mx-auto flex items-center justify-center').style('width:100%; height:auto;')
        #A:::foo & B:::bar --> C:::foobar
        #classDef foo stroke:#f00
        #classDef bar stroke:#0f0
        #classDef foobar stroke:#00f
        
        #flowchart LR
        #A & B --- C


