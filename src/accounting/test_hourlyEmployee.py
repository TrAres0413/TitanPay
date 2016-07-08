from unittest import TestCase
from src.accounting.hourly_employee import HourlyEmployee
from src.accounting.time_card import TimeCard


class TestHourlyEmployee(TestCase):

    def test_clock_in(self):
        hourly = HourlyEmployee('0', 'Chris', 'Capps', '333', '10', 'Pick Up')
        hourly.clock_in()
        timec = hourly.get_time_card()
        self.assertIsInstance(timec, TimeCard)

    def test_clock_out(self):
        hourly = HourlyEmployee('0', 'Chris', 'Capps', '333', '10', 'Pick Up')
        hourly.clock_in()
        hourly.clock_out()
        time = TimeCard.calculate_daily_pay()
        self.assertTrue(time >= 1)

    def test_pay(self):
        hourly = HourlyEmployee('0', 'Chris', 'Capps', '333', '10', 'Pick Up')
        hourly.clock_in()
        hourly.clock_out()
        time = TimeCard.calculate_daily_pay()
        self.assertTrue(time >= 1)
