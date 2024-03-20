from nicegui import app, ui
from components.header_footer import header_footer
from register.form import form

@ui.page('/register')
async def register_page():
    header_footer()
    ui.image('img/ow2/formbanner.avif').classes('w-full md:h-[200px] lg:h-[300px] xl:h-[300px] 2xl:h-[300px]')
    with ui.row().classes('w-full flex justify-center items-center text-center'):
        ui.label('PCL Registration Form') \
            .classes('w-full text-xl md:text-3xl lg:text-3xl xl:text-3xl 2xl:text-3xl font-mono text-[#ffc82e] mt-5')
    with ui.row().classes('w-full flex items-center justify-center'):
        form()
