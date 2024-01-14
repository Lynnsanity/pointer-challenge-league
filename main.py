from nicegui import app, ui

from home.home import home
import contact

ui.image('./img/ow2/tracer.jpg').tailwind.align_content('center').object_fit('cover')
ui.link('show page with fancy layout', home)

ui.run(title='PCL', favicon='./img/favicon/gaming.png')

