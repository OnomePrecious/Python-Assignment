class DiaryApp:

    def __init__(self):
        self.entries = {}


def menu():
    while True:
        print("""Welcome to My Diary App , what would you like to do?
        1-> create entry"
        2-> Lock diary
        3-> delete entry")
        4-> find entry by Id")
        5-> update entry""")


option = input("Enter your choice")
if option == 1:
    user_name = input("Enter your user name")
    password = input("Enter a strong password")
    print("entry created successfully")

elif option == 2:
    p
