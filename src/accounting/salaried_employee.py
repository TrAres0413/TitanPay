from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
import datetime


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, dues, salary, comm, payment_method):
        Employee.__init__(first_name, last_name, employee_id, dues, payment_method)
        self.__salary = salary
        self.__commission_rate = comm
        self.__weekly_receipt = []

    def get_salary(self):
        return self.__salary

    def get_commission(self):
        return self.__commission_rate

    def make_sale(self, sale_amt):
        date = datetime.date.today()
        amt = sale_amt
        receipt = Receipt(date, amt)
        self.__weekly_receipt.append(receipt)

    def calc_commission(self):
        commission = self.__commission_rate * self.__weekly_receipt
        return commission

    def pay(self):
        total_pay = 0
        for x in self.__weekly_receipt:
            total_pay += self.__salary + self.calc_commission()

        self.get_payment_method().pay(total_pay)







