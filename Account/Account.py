class Account:
    def __init__(self, name, number):
        self._balance = None
        self.name = name
        self.number = number

    def get_balance(self):
        return self._balance

    def balance(self, balance):
        if balance < 0.00:
            raise ValueError("Invalid amount exception")
        self._balance = balance


def deposit(self, amount: int):
    if amount >= 0:
        self._balance += amount
