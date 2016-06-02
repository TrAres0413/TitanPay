from src.accounting.employee import Employee


class HourlyEmployee(Employee):

    def __init__(self, first_name, last_name, employee, rate, dues):
        Employee.__init__(first_name, last_name, employee, dues)
        self.__hourly_rate = rate
