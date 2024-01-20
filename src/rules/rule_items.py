from nicegui import app, ui
import os

def read_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'md', file_name)

    with open(file_path, 'r') as file:
        content_variable = file.readlines()

    return content_variable

def display_file_content(file_name):
    file_content = read_file(file_name)

    file_content_html = '<br>'.join(file_content)

    ui.html(file_content_html).classes('font-mono list-disc text-sm sm:text-sm md:text-md lg:text-lg')

    ui.html().classes('pl-5 list-disc md:w-3/4 lg:w-1/2 xl:w-1/3')
