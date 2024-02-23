from decimal import Decimal


class Account:
    def __init__(self, name, balance: Decimal):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance < Decimal(0.00):
            raise ValueError("Invalid amount for balance")
        self.__balance = balance

    def __str__(self):
        return f"Name: {self.name} Balance: {self.__balance}"


a1 = Account('Precious',Decimal(100.0))
print(a1)
