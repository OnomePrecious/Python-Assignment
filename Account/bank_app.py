from Account import bank


class BankApp:

    def __init__(self):
        self.bank = bank.Bank("Precious Bank")

    def run_it(self):
        while True:
            print("""
            ***************************************************
            Welcome to my bank App, what would you like to do?",
        1-> Create new account
        2-> Deposit
        3-> Withdraw
        4-> Check balance
        5-> Remove customer
        6-> Transfer
        7-> Exit
            ******************************************************""")
            option = input("Enter your choice: ")
            if option == "1":
                first_name = input("Enter your first name: ")
                last_name = input("Enter your last name: ")
                pin = input("Enter your pin: ")
                print(self.bank.register_customer(first_name, last_name, pin))

            elif option == "2":
                try:
                    account_number = input("Enter your account number: ")
                    amount = float(input("Enter amount you want to deposit: "))
                except ValueError:
                    self.bank.deposit(account_number, amount)
                finally:
                    print(amount, "Deposited Successfully")

            elif option == "3":
                try:
                    account_number = input("Enter your account number: ")
                    pin = input("Enter pin: ")
                    amount = float(input("Enter amount to withdraw: "))
                except ValueError:
                    self.bank.withdraw(account_number, amount, pin)
                finally:
                    print(amount, "Withdrawn successfully")

            elif option == "4":
                try:
                    account_number = input("Enter account number: ")
                    pin = input("Enter your pin: ")
                except ValueError:
                    self.bank.check_balance(account_number, pin)
                finally:
                    print("Your balance is", self.bank.check_balance(account_number, pin))

            elif option == "5":
                try:
                    account_number = input("Enter account number to delete account: ")
                except ValueError:
                    self.bank.remove_account(account_number)
                finally:
                    print("account deleted successfully")

            elif option == "6":
                try:
                    account_number = input("Enter account number: ")
                    receiver_account_number = input("Enter account number: ")
                    amount = float(input("Enter amount to transfer: "))
                    pin = input("Enter pin: ")
                except ValueError:
                    self.bank.transfer(account_number, receiver_account_number, amount, pin)
                finally:
                    print("Transfer successful")

            elif option == "7":
                print("Exiting the bank app.")
                break

            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    app = BankApp()
    app.run_it()
