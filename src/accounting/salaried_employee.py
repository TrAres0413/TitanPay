from src.accounting.employee import Employee
from src.accounting.receipt import Receipt
from src.accounting.payment_method import PaymentMethod


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, dues, salary, comm, payment_method):
        Employee.__init__(first_name, last_name, employee_id, dues, payment_method)
        self.__salary = salary
        self.__commission_rate = comm
        self.__payment_method = payment_method
        self.__weekly_receipt = []

    def make_sale(self):
        receipt = Receipt()
        receipt.set_date()
        receipt.set_invoice()
        receipt.set_sale_amt()
        self.__weekly_receipt.append(receipt)

    def calc_commission(self):
        commission = self.__commission_rate * self.__weekly_receipt
        return commission

    def pay(self, salary, commission):
        payment_method = PaymentMethod()

        for x in self.__weekly_receipt:
            total_pay = salary + commission
            return total_pay
        payment_method.make_payment(total_pay)
        return payment_method






