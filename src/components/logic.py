from nicegui import app, ui, events
from email_validator import validate_email, EmailNotValidError

class Enable:
    def __init__(self) -> None:
        self.inputs = {}
        self.no_errors = True

    def empty(self, v):
        return v and len(v) > 0

    def char_limit(self, v):
        return v and len(v) < 35

    def message_char_limit(self, v):
        return v and len(v) < 512

    def is_valid_email(self, email):
      try:
        email_info = validate_email(email, check_deliverability=False)
        email = email_info.normalized
        return True
      except EmailNotValidError as e:
        print(f"Email validation error: {e}")
        return False


    def is_valid_phone_number(self, phone_number):
        try:
            phone_number = ''.join(c for c in phone_number if c.isdigit())
            if len(phone_number) != 10:
                return False
            return True
        except EmailNotValidError as e:
            print(f"Email validation error: {e}")
            return False

    def on_change(self, e):
        field_id = e.sender.id
        value = e.value.strip()  # Remove leading and trailing whitespace
        if '@' in value:  # Check if it's an email
            valid = self.is_valid_email(value)
        elif value.isdigit():  # Check if it's a phone number
            valid = self.is_valid_phone_number(value)
        else:  # Otherwise, treat it as a general input
            valid = self.empty(value) and self.char_limit(value)
        self.inputs[field_id] = valid
        self.update()

    def update(self):
        for i in self.inputs.values():
            if i is not True:
                self.no_errors = False
                break
        else:
            self.no_errors = True
