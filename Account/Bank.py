class Bank:
    def __init__(self, name, pin):
        self.receiver = None
        self.number = None
        self.last_name = None
        self.first_name = None
        self.pin = pin
        self.withdraw = None
        self.balance = None
        self.name = name
        self.list = []

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin):
        if pin == self.pin:
            self.balance -= amount
        raise ValueError("Incorrect Pin")

    def transfer(self, amount, pin):
        self.balance = -amount
        self.receiver += amount
        self.pin = pin

    def check_balance(self, balance, pin):
        self.balance = balance
        self.pin = pin

    def register_customer(self, first_name, last_name, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.pin = pin

    def remove_account(self, number, name):
        self.number = number
        self.name = name

    def find_account(self, number):
        self.number = number
