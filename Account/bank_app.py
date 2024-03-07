from Account import bank


class BankApp:

    def __init__(self):
        self.accounts = {}


def main():

    while True:
        print("""
        Welcome to my bank App, what would you like to do?",
    1-> Create new account
    2-> Deposit
    3-> Withdraw
    4-> Check balance
    5-> Remove customer
    6-> Transfer
    7-> Exit""")
        option = input("Enter your choice: ")
        if option == "1":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            account_number_generator = input("Enter account number: ")
            pin = input("Enter your pin: ")
            bank.Bank.register_customer(first_name + " " + last_name, account_number_generator, pin)


        elif option == "2":
            account_number = input("Enter your account number: ")
            amount = float(input("Enter amount you want to deposit: "))
            bank.Bank.deposit(self.accounts, account_number, amount)

        elif option == "3":
            account_number = input("Enter your account number: ")
            pin = input("Enter pin: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.Bank.withdraw(bank, account_number, amount, pin)

        elif option == "4":
            account_number = input("Enter account number: ")
            pin = input("Enter your pin: ")
            bank.Bank.check_balance(bank, account_number, pin)

        elif option == "5":
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            account_number_generator = input("Enter account number: ")
            pin = input("Enter your pin: ")
            bank.Bank.register_customer(first_name + " " + last_name, account_number_generator, pin)

        elif option == "6":
            account_number = input("Enter account number to delete account: ")
            bank.Bank.remove_account(self, account_number)

        elif option == "7":
            account_number = input("Enter account number: ")
            receiver_account_number = input("Enter account number: ")
            amount = float(input("Enter amount to transfer: "))
            pin = input("Enter pin: ")
            bank.Bank.transfer(self, account_number, receiver_account_number, amount, pin)

        elif option == "8":
            print("Exiting the bank app.")

        else:
            print("Invalid choice. Please choose a valid option.")

        if __name__ == "_main_":
            self.main()
