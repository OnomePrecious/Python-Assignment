from Diary import diary


class DiaryApp:
    def __init__(self):
        self.diary = diary.Diary("Precious Diary", "1234")

    def run_it(self):
        while True:
            print("""Welcome to My Diary App , what would you like to do?
        1-> create entry"
        2-> Lock diary
        3-> delete entry")
        4-> find entry by Id")
        5-> update entry""")
            option = int(input("Enter your choice: "))
            if option < 0 or option > 5:
                raise ValueError("invalid choice of option")
            if option == 1:
                body = input("Enter body of your diary: ")
                title = input("Enter the title of your diary: ")
                print(self.diary.create_entry(body, title))

            elif option == 2:
                password = input("Enter your password: ")
                print(self.diary.lock_diary(password))

            elif option == 3:
                body = input("Enter the body of your diary")
                entry_id = input("Enter the Id of the entry you want to delete")
                title = input("Enter the title of your diary")
                print(self.diary.update_entry(entry_id, title, body))

            elif option == 4:
                entry_id = input("Enter the ID of the entry you want to find")
                print(self.diary.find_entry_by_id(entry_id))

            elif option == 5:
                body = input("Enter the body of your diary")
                entry_id = input("Enter the ID of the entry you want to update")
                title = input("Enter the title of your diary")
                print(self.diary.update_entry(body, entry_id, title))


if __name__ == "__main__":
    app = DiaryApp()
    app.run_it()
