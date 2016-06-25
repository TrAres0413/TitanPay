from src.accounting.pickup_payment import PickupPayment
from src.accounting.mail_payment import MailPayment
from src.accounting.direct_deposit_payment import DirectDeposit
from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard


class PaymentMethod:
    def __init__(self, employee_id):
        self.__employee = employee_id
        self.__amt = TimeCard.calculate_daily_pay()
        '''I hope I put this in the right place'''

    def pay(self, amt):
        if Employee.get_payment_method() == "Pick Up":
            return PickupPayment
        elif Employee.get_payment_method() == "Mail":
            return MailPayment
        elif Employee.get_payment_method() == "Direct Deposit":
            return DirectDeposit.pay(amt)

