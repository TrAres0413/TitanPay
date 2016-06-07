from src.accounting.employee import Employee
from src.accounting.time_card import TimeCard


class HourlyEmployee(Employee):

    def __init__(self, first_name, last_name, employee_id, rate, dues):
        Employee.__init__(first_name, last_name, employee_id, dues)
        self.__hourly_rate = rate

    weekly_time = []

    def clockin(self):
        TimeCard.__init__()
        TimeCard.set_start_time()
        TimeCard.set_date()

