from src.accounting.time_card import TimeCard
from src.accounting.employee import Employee
from src.accounting.payment_method import PaymentMethod


class HourlyEmployee(Employee):

    def __init__(self, first_name, last_name, employee_id, rate, dues, payment_method):
        Employee.__init__(first_name, last_name, employee_id, dues, payment_method)
        self.__hourly_rate = rate
        self.__payment_method = payment_method
        self.__weekly_time_cards = []

    def clock_in(self):
        time_card = TimeCard(date)
        time_card.set_start_time()
        time_card.set_date()
        self.__weekly_time_cards.append(time_card)

    def clock_out(self):
        time_card = TimeCard(date)
        time_card.get_date()
        time_card.set_end_time()
        for x in self.__weekly_time_cards:
            if time_card.get_date == time_card.set_date:
                time_card.set_end_time()

    def pay(self, rate):
        payment_method = PaymentMethod()
        payment_method.make_payment()

        for x in self.__weekly_time_cards:
            time_card = TimeCard(date)
            time_card.calculate_daily_pay(rate)
            total_pay += time_card.calculate_daily_pay
            return total_pay
        return payment_method












        

