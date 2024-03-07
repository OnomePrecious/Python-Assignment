from datetime import datetime


class Entry:
    def __init__(self, user_id: int, title: str, body: str):
        self.user_id = user_id
        self.title = title
        self.body = body
        self.date_created = datetime

    def get_id(self):
        return self.user_id

    def set_title(self, new_title):
        self.title = new_title

    def set_body(self, new_body):
        self.body = new_body
