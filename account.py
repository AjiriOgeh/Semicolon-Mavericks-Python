class Account:
    pass

    def __init__(self, name: str, balance: int, pin: str, number: int):
        self._name = name
        self._balance = balance
        self._pin = pin
        self._number = number

    def get_name(self):
        return self._name

    def check_balance(self, pin: str):
        if self._pin != pin:
            raise ValueError  # make sure you change it to the proper one
        return self._balance

    def deposit(self, deposit_amount: int):
        if deposit_amount <= 0:
            raise ValueError
        self._balance += deposit_amount

    def withdraw(self, withdrawal_amount: int,pin: str):
        if self._pin != pin:
            raise ValueError
        if withdrawal_amount <= 0:
            raise ValueError
        if withdrawal_amount > self._balance:
            raise ValueError
        self._balance -= withdrawal_amount

    def get_number(self):
        return self._number

    def validate_pin(self, pin: str):
        return self._pin == pin
