from Account.exception.invalid_password_error import InvalidPasswordError
from Diary.entry import *


class Diary:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
        self.locked = False
        self.entries = []
        self.id = 1

    def lock_diary(self, password) -> None:
        self.validate_password(password)
        self.locked = True

    def unlock_diary(self):
        self.locked = False

    def validate_password(self, password):
        if self.password != password:
            raise InvalidPasswordError("input correct password")
        else:
            self.password = password

    def create_entry(self, title, body):
        entry1 = Entry(self.id, title, body)
        self.id += 1
        self.entries.append(entry1)
        return "new entry created"

    def delete_entry(self, user_id):
        for entry in self.entries:
            if entry.get_id() == user_id:
                self.entries.remove(entry)
            return f"entry successfully deleted"

    def find_entry_by_id(self, user_id) -> Entry:
        for entry in self.entries:
            if entry.get_id() == user_id:
                return entry

    def update_entry(self, i_d, title, body):
        found_entry = self.find_entry_by_id(i_d)
        found_entry.set_body(body)
        found_entry.set_title(title)
        return "entry updated successfully"
