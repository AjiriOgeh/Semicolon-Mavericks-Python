from unittest import TestCase
import account


class Test(TestCase):

    def test_check_balance(self):
        my_account = account.Account("John Doe", 0, "1234", 12345678)
        pin = "1234"
        my_account.check_balance(pin)
        self.assertEqual(0, my_account.check_balance(pin))

    def test_deposit(self):
        my_account = account.Account("John Doe", 0, "1234", 12345678)
        deposit_amount = 5000
        pin = "1234"
        my_account.deposit(deposit_amount)
        self.assertEqual(5000, my_account.check_balance(pin))

    def test_withdraw(self):
        my_account = account.Account("John Doe", 0, "1234", 12345678)
        deposit_amount = 5000
        pin = "1234"
        my_account.deposit(deposit_amount)
        self.assertEqual(5000, my_account.check_balance(pin))

        withdrawal_amount = 2500
        my_account.withdraw(withdrawal_amount, pin)

        self.assertEqual(2500, my_account.check_balance(pin))


