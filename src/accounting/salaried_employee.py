from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
import datetime


class SalariedEmployee(Employee):
    def __init__(self,employee_id, first_name, last_name, dues, salary, comm, payment_method):
        Employee.__init__(employee_id, first_name, last_name, dues, payment_method)
        self.__salary = salary
        self.__commission_rate = comm
        self.__total_pay = 0
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

    def get_sales(self):
        return self.__weekly_receipt

    def calc_commission(self):
        commission = self.__commission_rate * self.__weekly_receipt
        return commission

    def pay(self):
        for x in self.__weekly_receipt:
            self.__total_pay += self.__salary + self.calc_commission()
            self.get_payment_method().pay(self.__total_pay)

    def get_total_pay(self):
        return self.__total_pay








