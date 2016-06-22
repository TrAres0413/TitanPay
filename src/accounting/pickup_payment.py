from src.accounting.payment_method import PaymentMethod
from src.accounting.time_card import TimeCard
from src.accounting.employee import Employee


class PickupPayment(PaymentMethod):
    def __init__(self, employee_id, amt):
        self.__employee = employee_id
        print("A check for " + amt + "is waiting for " + Employee.get_full_name() + "at the PostMaster.")
