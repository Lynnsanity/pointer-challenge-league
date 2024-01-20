#!/usr/bin/env python3


### CODE FOR WITHOUT LOGIN UPON RELEASE
#from nicegui import app, ui
#from home import home_page
#
#ui.image('./img/ow2/tracer.jpg').tailwind.align_content('center').object_fit('cover')
#ui.link('show page with fancy layout', home_page)
#ui.run(title='PCL', favicon='./img/favicon/gaming.png')

import os
from typing import Optional

from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from nicegui import Client, app, ui

from rules import rules_page
from home import home_page

user_env_var = os.environ.get('AUTH_USER')
password_env_var = os.environ.get('AUTH_PASS')
passwords = {user_env_var: password_env_var} if user_env_var and password_env_var else {}

# passwords = {'user1': 'pass1', 'user2': 'pass2'}
storage_secret = os.environ.get('STORAGE_SECRET')
unrestricted_page_routes = {'/login'}


class AuthMiddleware(BaseHTTPMiddleware):
    """This middleware restricts access to all NiceGUI pages.
#
    It redirects the user to the login page if they are not authenticated.
    """

    async def dispatch(self, request: Request, call_next):
        if not app.storage.user.get('authenticated', False):
            if request.url.path in Client.page_routes.values() and request.url.path not in unrestricted_page_routes:
                app.storage.user['referrer_path'] = request.url.path  # remember where the user wanted to go
                return RedirectResponse('/login')
        return await call_next(request)


app.add_middleware(AuthMiddleware)


@ui.page('/')
def index() -> None:
    with ui.column().classes('absolute-center items-center'):
        ui.label(f'Hello {app.storage.user["username"]}!').classes('text-2xl')
        ui.button(on_click=lambda: (app.storage.user.clear(), ui.open('/login')), icon='logout').props('outline round')

@ui.page('/login')
def login() -> Optional[RedirectResponse]:
    def try_login() -> None:  # local function to avoid passing username and password as arguments
        if passwords.get(username.value) == password.value:
            app.storage.user.update({'username': username.value, 'authenticated': True})
            ui.open(app.storage.user.get('referrer_path', '/home'))  # go back to where the user wanted to go
        else:
            ui.notify('Wrong username or password', color='negative')

    if app.storage.user.get('authenticated', False):
        return RedirectResponse('/')
    with ui.card().classes('absolute-center'):
        username = ui.input('Username').on('keydown.enter', try_login)
        password = ui.input('Password', password=True, password_toggle_button=True).on('keydown.enter', try_login)
        ui.button('Log in', on_click=try_login)


ui.run(storage_secret=storage_secret)
