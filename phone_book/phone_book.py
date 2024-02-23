phone_book = {}


def add_contact(name, number):
    phone_book[name] = number
    return 'Contact saved'


def search_contact(name):
    if name in phone_book:
        return f"Phone number: {phone_book[name]}"
    return "Contact not found"


def main():
    while True:
        print("1. Add contact")
        print("2. Search contact")
        print('3. Exit')

        option = input("Select an option: ")

        if option == "1":
            name = input('Enter contact name: ')
            number = int(input("Enter contact number"))
            add_contact(name, number)
        elif option == "2":
            name = input("Enter name to search")
            search_contact(name)
        elif option == "3":
            return "Exiting the phonebook app."
        else:
            return "Invalid choice. Please choose a valid option."
