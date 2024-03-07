from Diary import diary


class Diaries:

    def __init__(self):
        self.diaries = list()

    def add(self, user_name, password):
        diary1 = diary.Diary(user_name, password)
        self.diaries.append(diary1)
        return "an entry added"

    def find_by_user_name(self, user_name):
        if user_name in self.diaries:
            return user_name
        else:
            return "not found"

    def delete(self, user_name, password):
        for entry in self.diaries:
            if user_name and password in self.diaries:
                self.diaries.remove(entry)
