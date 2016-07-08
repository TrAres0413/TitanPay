from unittest import TestCase
from src.accounting.salaried_employee import SalariedEmployee


class TestSalariedEmployee(TestCase):
    def __init__(self):
        super().__init__()
        self.__emp = SalariedEmployee(0, 'Chris', 'Capps', 10, 333, .05, "Pick Up")

    def test_get_salary(self):
        test = self.__emp.get_salary()
        self.assertTrue(test >= 1)

    def test_get_commission(self):
        test = self.__emp.get_commission()
        self.assertTrue(test <= 1)

    def test_make_sale(self):
        self.__emp.make_sale(10)
        test_len = len(self.__emp.get_sales())
        self.assertTrue(test_len == 1)

    def test_calc_commission(self):
        self.__emp.make_sale(10)
        test_comm = self.__emp.calc_commission()
        self.assertTrue(test_comm >= 1)

    def test_pay(self):
        self.__emp.make_sale(10)
        test_pay = self.__emp.pay()
        self.assertEqual(test_pay, self.__emp.get_total_pay())
