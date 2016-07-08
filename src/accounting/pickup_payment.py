from src.accounting.payment_method import PaymentMethod


class PickupPayment(PaymentMethod):
    def __init__(self, employee, amt):
        self.__employee = employee
        self.__amt = amt

    def pay(self, amt):
        return "A check for " + amt + "is waiting for " + self.__employee.get_full_name() + "at the PostMaster."

