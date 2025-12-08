from enum import Enum


class AccountStatus(Enum):
    ACTIVE = 100
    CLOSED = 200
    BLOCKED = 300

class account(object):
    def __init__(self, iban: str, balance : float=0.0, status: AccountStatus = AccountStatus.ACTIVE):
        self.__iban = iban
        self.__balance = balance

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def iban(self) -> str:
        return self.__iban

    @iban.setter
    def iban(self, new_iban: str) -> None:
        self.__iban = new_iban

    def deposit(self, amount: float) -> None:
        # validation
        if amount <= 0:
            raise ValueError('amount must be positive')
        # business logic
        self.__balance += amount


    def withdraw(self, amount: float) -> None:
        # validation
        if amount <= 0:
            raise ValueError('amount must be positive')
        # business rule
        if amount > self.__balance:
            raise ValueError('amount cannot be greater than balance')
        self.__balance -= amount

    def __str__(self) -> str:
        return f"Account [iban:{self.__iban}, balance:{self.__balance}]"
acc1 : account = account(iban="tr1", balance=1000,status = "closd")
acc2 : account = account(iban="tr2")
acc1.withdraw(700) # withdraw(acc1,700)
# acc1.balance -= 1_000_000
acc1.iban = "tr3"
print(acc1.balance)
print(acc1)
print(str(acc1))