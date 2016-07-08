from unittest import TestCase
from src.accounting.hourly_employee import HourlyEmployee
from src.accounting.time_card import TimeCard


class TestTimeCard(TestCase):
    def test_get_date(self):
        test_card = TimeCard(11/21/1983)
        test_card.get_date()
        self.assertEqual(test_card, 11/21/1983)

    def test_calculate_daily_pay(self):
        hourly = HourlyEmployee('0', 'Chris', 'Capps', '333', '10', 'Pick Up')
        hourly.clock_in()
        hourly.clock_out()
        time = TimeCard.calculate_daily_pay()
        self.assertTrue(time >= 1)
