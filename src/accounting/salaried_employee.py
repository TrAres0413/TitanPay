from src.accounting.employee import Employee
from src.accounting.receipt import Receipt


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, dues, salary, comm):
        Employee.__init__(first_name, last_name, employee_id, dues)
        self.__salary = salary
        self.__commission_rate = comm
        self.__weekly_receipt = []

    def make_sale(self):
        Receipt.get_receipt()
        self.__weekly_receipt.append()

    def calc_commission(self):
        commission = self.__commission_rate * self.__weekly_receipt
        return commission





