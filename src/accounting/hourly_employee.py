from src.accounting.time_card import TimeCard
from src.accounting.employee import Employee


class HourlyEmployee(Employee):

    def __init__(self, first_name, last_name, employee_id, rate, dues):
        Employee.__init__(first_name, last_name, employee_id, dues)
        self.__hourly_rate = rate
        self.__weekly_time = []

    def clock_in(self):
        TimeCard.__init__()
        TimeCard.set_start_time()
        TimeCard.set_date()

    def clock_out(self):
        TimeCard.set_end_time()

    def pay(self):
        TimeCard.calculate_daily_pay()

        

