from src.accounting.employee import Employee
from src.accounting.address import Address
from src.accounting.payment_method import PaymentMethod


class MailPayment(PaymentMethod):
    def __init__(self, employee_id, amt):
        self.__employee = employee_id
        self.__amt = amt

    def pay(self, amt):
        address = Address.get_address()
        return "Mailing a check to " + Employee.get_full_name() + "for $" + amt + "to " + address + "."
