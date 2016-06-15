

class TimeCard:
    def __init__(self, start, end, date):
        self.__date = date
        self.__start_time = start
        self.__end_time = end

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_start_time(self, start):
        self.__start_time = start

    def set_end_time(self, end):
        self.__end_time = end

    def calculate_daily_pay(self, rate):
        hours = self.__end_time - self.__start_time

        if hours <= 8:
            daily_pay = hours * rate
            return daily_pay

        if hours > 8:
            daily_pay = (rate * 8) + (1.5*rate * (hours - 8))
            return daily_pay
