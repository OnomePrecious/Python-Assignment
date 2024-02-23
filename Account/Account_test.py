import unittest
import Account


class MyTestCase(unittest.TestCase):
    def test_that_new_account_balance_is_zero(self):
        precious_account: Account = Account
        balance = 0
        self.assertEqual(balance, precious_account.get_balance())  # add assertion here

    def test_deposit_10k_balance_is_10k(self):
        precious_account: Account = Account
        precious_account.deposit(10_000)
        self.assertEqual(10_000, precious_account.get_balance())

    def test_deposit_10k_twice_balance_is_20k(self):
        precious_account: Account = Account
        precious_account.deposit(10_000)
        precious_account.deposit(10_000)
        result = 20_000
        self.assertEqual(20_000, result)

    def test_deposit_negative_amount_balance_is_not_changed(self):
        precious_account: Account = Account
        precious_account.deposit(-10_000)
        self.assertEqual(-10_000, precious_account.get_balance())
