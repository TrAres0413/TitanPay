from src.accounting.payment_method import PaymentMethod
from src.accounting.employee import Employee


class PickupPayment(PaymentMethod):
    def __init__(self, employee_id, amt):
        self.__employee = employee_id
        self.__amt = amt

    def pay(self, amt):
        return "A check for " + amt + "is waiting for " + Employee.get_full_name() + "at the PostMaster."
