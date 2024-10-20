import Account.account


class Bank:
    def __init__(self, bank_name):
        self.accounts: list = []
        self.name = bank_name
        self.account_number_generator = 1000

    def register_customer(self, first_name, last_name, pin):
        new_account = Account.account.Account(first_name + " " + last_name, self.account_number_generator, pin)
        self.account_number_generator += 1
        self.accounts.append(new_account)
        return new_account

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(account_number,amount)

    def withdraw(self, account_number, amount, pin):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, account_number, receiver_account_number, amount, pin):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)
        receiver = self.find_account(receiver_account_number)
        receiver.deposit(amount)

    def check_balance(self, account_number, pin):
        balance = self.find_account(account_number)
        return balance.check_balance(account_number, pin)

    def find_account(self, number):
        for account in self.accounts:
            if account.get_account_number == number:
                return account

    def remove_account(self, number):
        for account in self.accounts:
            if account.get_account_number == number:
                return account
