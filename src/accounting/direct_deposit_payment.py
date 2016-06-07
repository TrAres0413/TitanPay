from src.accounting.payment_method import PaymentMethod
from src.accounting.bank_account import BankAccount


class DirectDepositStatement:
    def __init__(self, amt):
        self.__amt = amt

    def make_deposit(self):
        return BankAccount.deposit()

