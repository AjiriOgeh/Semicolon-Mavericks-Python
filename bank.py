import random

from account import Account


class Bank:
    pass

    accounts = []

    def __init__(self, name):
        self._name = name

    def register_account(self, first_name: str, last_name: str, pin: str):
        name = first_name + " " + last_name
        number = self.generate_account_number
        account = Account(name, 0, pin, number)
        self.accounts.append(account)
        return account

    @property
    def generate_account_number(self):
        return random.randint(1_000_000_000, 1_999_999_999)

    def get_number_of_accounts(self):
        return len(self.accounts)

    def find_account(self, number):
        for account in self.accounts:
            if account.get_number() == number:
                return account
        return None

    def check_balance(self, number: int, pin: str):
        if self.find_account(number) is None:
            raise ValueError
        my_account = self.find_account(number)
        return my_account.check_balance(pin)

    def remove_account(self, number: int, pin: str):
        if self.find_account(number) is None:
            raise ValueError
        my_account = self.find_account(number)
        if my_account.validate_pin:
            self.accounts.remove(my_account)

    def deposit(self, number: int, deposit_amount: int):
        if self.find_account(number) is None:
            raise ValueError
        my_account = self.find_account(number)
        my_account.deposit(deposit_amount)

    def withdraw(self, number: int, withdrawal_amount: int, pin):
        if self.find_account(number) is None:
            raise ValueError
        my_account = self.find_account(number)
        my_account.withdraw(withdrawal_amount, pin)

    def transfer(self, sender_number: int, receiver_number: int, transfer_amount: int, sender_account_pin: str):
        if self.find_account(sender_number) is None:
            raise ValueError
        if self.find_account(receiver_number) is None:
            raise ValueError
        sender_account = self.find_account(sender_number)
        sender_account.withdraw(transfer_amount, sender_account_pin)
        receiver_account = self.find_account(receiver_number)
        receiver_account.deposit(transfer_amount)