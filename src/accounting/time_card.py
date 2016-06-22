import datetime


class TimeCard:
    def __init__(self, date):
        self.__date = date

    def clock_in(self):
        self.__start_time = datetime.datetime.now().today()

    def clock_out(self):
        self.__end_time = datetime.datetime.now().today()

    def calculate_daily_pay(self, rate):
        hours = self.__end_time - self.__start_time

        if hours <= 8:
            daily_pay = hours * rate
            return daily_pay

        if hours > 8:
            daily_pay = (rate * 8) + (1.5*rate * (hours - 8))
            return daily_pay
