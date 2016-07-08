from src.accounting.hourly_employee import HourlyEmployee


class TimeCard:
    def __init__(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def calculate_daily_pay(self):
        hours = HourlyEmployee.clock_out() - HourlyEmployee.clock_in()

        if hours <= 8:
            daily_pay = hours * HourlyEmployee.get_hourly_rate()
            return daily_pay

        if hours > 8:
            daily_pay = (HourlyEmployee.get_hourly_rate() * 8) + (1.5 * HourlyEmployee.get_hourly_rate() * (hours - 8))
            return daily_pay
