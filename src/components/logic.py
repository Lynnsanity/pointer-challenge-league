from nicegui import app, ui, events
from email_validator import validate_email, EmailNotValidError

# this is a class for checking inputs as theyre entered in
# to see if they're valid or not
class Enable:
    def __init__(self) -> None:
        self.inputs = {}
        self.no_errors = True

    # input must be greater than 0 characters
    def empty(self, v):
        return v and len(v) > 0

    # input can't be greater than 35 characters
    def char_limit(self, v):
        return v and len(v) < 35
    
    def optional_char_limit(self, v):
        if len(v) == 0:
            return True
        return v and len(v) < 35

    def validate_optional_field(self, value):
        if value.strip():
            return self.optional_char_limit(value)
        return True

    # for message summary specifically, we want users to be
    # able to put up to 512 characters
    def message_char_limit(self, v):
        return v and len(v) < 512

    # code for checking if a users email inputted is valid
    def is_valid_email(self, email):
      try:
        email_info = validate_email(email, check_deliverability=False)
        email = email_info.normalized
        return True
      except EmailNotValidError as e:
        print(f"Email validation error: {e}")
        return False

    # code for checking phone numbers, no international
    def is_valid_phone_number(self, phone_number):
        try:
            phone_number = ''.join(c for c in phone_number if c.isdigit())
            if len(phone_number) != 10:
                return False
            return True
        except EmailNotValidError as e:
            print(f"Email validation error: {e}")
            return False

    # every time an input is changed in contact form, this gets re-run
    # to check the input against the function it needs to be valid
    def contact_on_change(self, e):
        field_id = e.sender.id
        value = e.value.strip()
        if '@' in value:
            valid = self.is_valid_email(value)
        elif value.isdigit():
            valid = self.is_valid_phone_number(value)
        else:
            valid = self.empty(value) and self.message_char_limit(value)
        self.inputs[field_id] = valid
        self.update()

    # every time an input is changed in registration form, this gets re-run
    # to check the input against the function it needs to be valid
    def registration_on_change(self, e):
        field_id = e.sender.id
        value = e.value.strip()
        if '@' in value:
            valid = self.is_valid_email(value)
        elif any(char.isdigit() for char in value) and sum(char.isdigit() for char in value) == 10:
            valid = self.empty(value) and self.char_limit(value)
        else:
            valid = self.empty(value) and self.char_limit(value)
        self.inputs[field_id] = valid
        self.update()

    def registration_on_optional_change(self, e):
        field_id = e.sender.id
        value = e.value.strip()
        if '@' in value:
            valid = self.is_valid_email(value)
        elif any(char.isdigit() for char in value) and sum(char.isdigit() for char in value) == 10:
            valid = self.empty(value) and self.optional_char_limit(value)
        else:
            valid = self.optional_char_limit(value)
        self.inputs[field_id] = valid
        self.update()

    # update the input to have no errors if passes checked
    def update(self):
        for i in self.inputs.values():
            if i is not True:
                self.no_errors = False
                break
        else:
            self.no_errors = True
