from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
from src.accounting.payment_method import PaymentMethod
import datetime


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, dues, salary, comm, payment_method):
        Employee.__init__(first_name, last_name, employee_id, dues, payment_method)
        self.__salary = salary
        self.__commission_rate = comm
        self.__weekly_receipt = []

    def make_sale(self):
        receipt = Receipt()
        receipt.set_invoice()
        receipt.set_sale_amt()
        self.__weekly_receipt.append(receipt)

    def calc_commission(self):
        commission = self.__commission_rate * self.__weekly_receipt
        return commission

    def pay(self):
        total_pay = 0
        for x in self.__weekly_receipt:
            total_pay += self.__salary + self.calc_commission()

        self.get_payment_method().pay(total_pay)







