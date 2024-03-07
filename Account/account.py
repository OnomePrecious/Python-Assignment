from Account.exception.insufficient_funds_error import InsufficientFundsError
from Account.exception.invalid_amount_exception import InvalidAmountError
from Account.exception.invalid_pin_error import InvalidPinError


class Account:
    def __init__(self, account_name, account_number, pin):
        self.balance = 0
        self._name = account_name
        self._number = account_number
        self._pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise InvalidAmountError("input valid amount")

    def transfer(self, receiver_account, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise InvalidAmountError("input valid amount to transfer")

    def withdraw(self, amount, pin):
        if amount < 0:
            raise InvalidAmountError("input valid amount")
        elif amount > self.balance:
            raise InsufficientFundsError("Insufficient balance")
        elif self._pin != pin:
            raise InvalidPinError("Incorrect pin")
        else:
            self.balance -= amount

    def check_balance(self, pin):
        if self._pin != pin:
            raise InvalidPinError("Incorrect pin")
        return self.balance

    def get_account_number(self):
        return self._number
