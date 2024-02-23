from unittest import TestCase

import bank

import account


class Test(TestCase):

    def test_find_account(self):
        my_bank = bank.Bank("Bank")
        my_account = my_bank.register_account("John", "Doe", "1234")

        account_number = my_account.get_number()
        valid_pin = "1234"

        self.assertEqual(my_account, my_bank.find_account(account_number))
        self.assertEqual(1, my_bank.get_number_of_accounts())

    def test_find_non_existent_account(self):
        my_bank = bank.Bank("Bank")
        my_account = my_bank.register_account("John", "Doe", "1234")

        account_number = 2_134_567_890
        self.assertEqual(None, my_bank.find_account(account_number))

    def test_check_balance(self):
        my_bank = bank.Bank("Bank")
        my_account = my_bank.register_account("John", "Doe", "1234")

        account_number = my_account.get_number()
        valid_pin = "1234"

        self.assertEqual(my_account, my_bank.find_account(account_number))
        self.assertEqual(0, my_bank.check_balance(account_number, valid_pin))

    def test_remove_account(self):
        my_bank = bank.Bank("Bank")
        my_account = my_bank.register_account("John", "Doe", "1234")

        account_number = my_account.get_number()
        valid_pin = "1234"

        self.assertEqual(my_account, my_bank.find_account(account_number))
        self.assertEqual(1, my_bank.get_number_of_accounts())

        my_bank.remove_account(account_number, valid_pin)

        self.assertEqual(None, my_bank.find_account(account_number))
        self.assertEqual(0, my_bank.get_number_of_accounts())

    def test_deposit(self):
        my_bank = bank.Bank("Bank")
        my_account = my_bank.register_account("John", "Doe", "1234")

        account_number = my_account.get_number()
        valid_pin = "1234"

        self.assertEqual(0, my_bank.check_balance(account_number, valid_pin))
        self.assertEqual(my_account, my_bank.find_account(account_number))

        my_bank.deposit(account_number, 5000)
        self.assertEqual(5000, my_bank.check_balance(account_number, valid_pin))

    def test_withdraw(self):
        my_bank = bank.Bank("Bank")
        my_account = my_bank.register_account("John", "Doe", "1234")

        account_number = my_account.get_number()
        valid_pin = "1234"

        self.assertEqual(0, my_bank.check_balance(account_number, valid_pin))
        self.assertEqual(my_account, my_bank.find_account(account_number))

        my_bank.deposit(account_number, 5000)
        self.assertEqual(5000, my_bank.check_balance(account_number, valid_pin))

        withdrawal_amount = 2500

        my_bank.withdraw(account_number, withdrawal_amount, valid_pin)
        self.assertEqual(2500, my_bank.check_balance(account_number, valid_pin))

    def test_transfer(self):
        my_bank = bank.Bank("Bank")
        sender_account = my_bank.register_account("John", "Doe", "1234")
        sender_account_number = sender_account.get_number()
        sender_account_valid_pin = "1234"

        receiver_account = my_bank.register_account("Jane", "Doe", "5678")
        receiver_account_number = receiver_account.get_number()
        receiver_account_valid_pin = "5678"

        self.assertEqual(2, my_bank.get_number_of_accounts())

        my_bank.deposit(sender_account_number, 10000)
        self.assertEqual(10000, my_bank.check_balance(sender_account_number, sender_account_valid_pin))

        transfer_amount = 7500
        my_bank.transfer(sender_account_number, receiver_account_number, transfer_amount, sender_account_valid_pin)

        self.assertEqual(2500, my_bank.check_balance(sender_account_number, sender_account_valid_pin))
        self.assertEqual(7500, my_bank.check_balance(receiver_account_number, receiver_account_valid_pin))


