from nicegui import ui, events

class Logic:
    def __init__(self):
        self.selected_value = 0
        self.subone_firstname = ui.input('First Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subone_lastname = ui.input('Last Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subone_ign = ui.input('In Game Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subone_firstname.visible = False
        self.subone_lastname.visible = False
        self.subone_ign.visible = False
        self.subtwo_firstname = ui.input('First Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subtwo_lastname = ui.input('Last Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subtwo_ign = ui.input('In Game Name') \
            .props('outlined v-model="text" color=amber dark') \
            .classes('w-full')
        self.subtwo_firstname.visible = False
        self.subtwo_lastname.visible = False
        self.subtwo_ign.visible = False

    def update_visibility(self, e: events.ValueChangeEventArguments):
        self.selected_value = e.value
        self.update_inputs()

    def update_inputs(self):
        # clear all inputs
        self.subone_firstname.visible = False
        self.subone_lastname.visible = False
        self.subone_ign.visible = False
        self.subtwo_firstname.visible = False
        self.subtwo_lastname.visible = False
        self.subtwo_ign.visible = False

        # shows input 1 if 1 or 2 is selected
        if self.selected_value >= 1:
            self.subone_firstname.visible = True
            self.subone_lastname.visible = True
            self.subone_ign.visible = True

        # shows input2 if 2 is selected
        if self.selected_value == 2:
            self.subtwo_firstname.visible = True
            self.subtwo_lastname.visible = True
            self.subtwo_ign.visible = True

