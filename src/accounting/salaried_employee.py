from src.accounting.employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, first_name, last_name, employee_id, dues, salary, comm):
        Employee.__init__(first_name, last_name, employee_id, dues)
        self.__salary = salary
        self.__commission_rate = comm

    sales_receipts = []


