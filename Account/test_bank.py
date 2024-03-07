import unittest

from Account import bank


class MyTestCase(unittest.TestCase):

    def test_create_account(self):
        precious_bank = bank.Bank("Precious bank")
        precious_bank.register_customer("Onome", "Precious", "1234")
        self.assertEqual("Account successfully created", precious_bank.register_customer("Onome", "Precious", "1234"))

    def test_deposit(self):
        precious_bank = bank.Bank("Precious bank")
        self.assertEqual(0, precious_bank.check_balance("1000", "1234"))
        precious_bank.deposit(1000, 1000)
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


