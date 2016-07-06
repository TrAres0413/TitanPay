from src.accounting.time_card import TimeCard
from src.accounting.employee import Employee
import datetime


class HourlyEmployee(Employee):

    def __init__(self, first_name, last_name, employee_id, rate, dues, payment_method):
        Employee.__init__(first_name, last_name, employee_id, dues, payment_method)
        self.__hourly_rate = rate
        self.__weekly_time_cards = []

    def get_hourly_rate(self):
        return self.__hourly_rate

    def clock_in(self):
        today = datetime.date.today()
        time_card = TimeCard(today)
        time_card.clock_in()
        self.__weekly_time_cards.append(time_card)

    def clock_out(self):
        for x in self.__weekly_time_cards:
            if x.get_date() == datetime.date.today():
                x.clock_out()

    def pay(self, start_date, end_date):
        total_pay = 0
        for x in self.__weekly_time_cards:
            if x.get_date() >= start_date <= end_date:
                total_pay += x.calculate_daily_pay(self.__hourly_rate)

        self.get_payment_method().pay(total_pay)
















        

