from src.accounting.payment_method import PaymentMethod
from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard


class PickupPayment:
    def __init__(self):
        amt = TimeCard.calculate_daily_pay()
        print("A check for " + amt + "is waiting for " + Employee.get_full_name() + "at the PostMaster.")
