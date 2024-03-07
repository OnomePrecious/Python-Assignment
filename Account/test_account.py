import unittest
from Account import account
from Account.exception.insufficient_funds_error import InsufficientFundsError
from Account.exception.invalid_amount_exception import InvalidAmountError
from Account.exception.invalid_pin_error import InvalidPinError


class MyTestCase(unittest.TestCase):
    def test_that_new_account_balance_is_zero(self):
        precious_account = account.Account("Precious", 5667, '1234')
        self.assertEqual(0, precious_account.check_balance('1234'))

    def test_deposit_negative_amount_raise_invalid_amount_exception(self):
        precious_account = account.Account("Precious", 5667, '1234')
        self.assertRaises(InvalidAmountError, lambda: precious_account.deposit(-10_000))

    def test_deposit_10k_balance_is_10k(self):
        precious_account = account.Account("Precious", 5667, '1234')
        precious_account.deposit(10_000)
        self.assertEqual(10_000, precious_account.check_balance('1234'))

    def test_deposit_10k_twice_balance_is_20k(self):
        precious_account = account.Account("Precious", 5667, '1234')
        precious_account.deposit(10_000)
        precious_account.deposit(10_000)
        self.assertEqual(20_000, precious_account.check_balance('1234'))

    def test_withdraw(self):
        precious_account = account.Account("Precious", 5667, '1234')
        precious_account.deposit(10_000)
        precious_account.withdraw(5_000, '1234')
        self.assertEqual(5_000, precious_account.check_balance('1234'))

    def test_that_withdrawal_cannot_pass_balance(self):
        precious_account = account.Account("Precious", 5667, '1234')
        precious_account.deposit(10_000)
        self.assertRaises(InsufficientFundsError, lambda: precious_account.withdraw(12_000, '1234'))

    def test_that_negative_amount_cannot_be_withdrawn(self):
        precious_account = account.Account("Precious", 5667, '1234')
        precious_account.deposit(10_000)
        self.assertRaises(InvalidAmountError, lambda: precious_account.withdraw(-12_000, '1234'))

    def test_withdraw_with_incorrect_pin_raises_invalid_pin_error(self):
        precious_account = account.Account("Precious", 5667, '1234')
        precious_account.deposit(10_000)
        self.assertRaises(InvalidPinError, lambda: precious_account.withdraw(1_000, '4321'))

    def test_check_balance_with_wrong_pin_raises_invalid_pin_error(self):
        precious_account = account.Account("Precious", 5667, '1234')
        precious_account.deposit(10_000)
        self.assertRaises(InvalidPinError, lambda: precious_account.check_balance('4321'))