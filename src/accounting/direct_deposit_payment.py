from src.accounting.payment_method import PaymentMethod


class DirectDeposit(PaymentMethod):
    def __init__(self, employee_id, bank_acct):
        PaymentMethod.__init__(employee_id)
        self.__bank = bank_acct

    def pay(self, amt):
        self.__bank.deposit()
