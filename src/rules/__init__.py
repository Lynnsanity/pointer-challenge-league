from nicegui import app, ui

from components.header_footer import header_footer
from rules.rule_items import display_file_content


@ui.page('/rules')
async def rules_page():
    header_footer()

    ui.query('body').style('background-color: #181818')

    with ui.tabs().classes('w-full text-[#FFC82e] bg-[#512698]') as tabs:
        one = ui.tab('Stakeholders')
        two = ui.tab('Participant Conduct')
        three = ui.tab('Competition Rules')
        four = ui.tab('Scoring Rubric')
        five = ui.tab('Prizes')

    with ui.tab_panels(tabs, value=one).classes('w-full bg-[#27282b] text-white'):
        with ui.tab_panel(one).classes('flex items-center justify-center text-left'):
            display_file_content('stakeholders.html')
        with ui.tab_panel(two):
            display_file_content('participant_conduct.html')
        with ui.tab_panel(three):
            display_file_content('competition_rules.html')
        with ui.tab_panel(four):
            display_file_content('scoring_rubric.html')
        with ui.tab_panel(five):
            display_file_content('prizes.html')
