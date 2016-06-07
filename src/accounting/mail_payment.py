from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard
from src.accounting.address import Address


class MailPayment:
    def __init__(self):
        amt = TimeCard.calculate_daily_pay()
        address = Address.get_address()
        print("Mailing a check to " + Employee.get_full_name() + "for $" + amt + "to " + address + ".")
