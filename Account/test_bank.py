import unittest

from Account import bank
from Account.account import Account


class MyTestCase(unittest.TestCase):

    def test_create_account(self):
        precious_bank = bank.Bank("Precious bank")
        precious_bank.register_customer("Onome", "Precious", "1234")
        self.assertEqual(1001, precious_bank.account_number_generator)

    def test_deposit(self):
        precious_bank = bank.Bank("Precious bank")
        # precious_bank.find_account("1000")
        precious_bank.deposit(1000, 12_00)
        self.assertEqual(12_000, precious_bank.check_balance(1000, "1234"))

    def test_withdraw(self):
        precious_bank = bank.Bank("Precious bank")
        precious_bank.deposit(1000, 12_000)
        precious_bank.withdraw(1000, 5_000, "1234")
        self.assertEqual(7_000, precious_bank.check_balance(1000, "1234"))

    def test_transfer(self):
        precious_bank = bank.Bank("Precious bank")
        precious_bank.deposit(1000, 5_000)
        precious_bank.transfer(1000, 1001, 2_000, "1234")
        precious_bank.withdraw(1000, 2_000, "1234")
        precious_bank.deposit(1001, 2_000)
        self.assertEqual(3_000, precious_bank.check_balance(1000, "1234"))

    def test_checkBalance(self):
        precious_bank = bank.Bank("Precious bank")
        precious_bank.deposit(1000, 12_000)
        self.assertEqual(12_000, precious_bank.check_balance(1000, "1234"))
