class SalariedEmployee:

    def __init__(self, employee, first, last, rate, commission, dues):
            self.__employee_id = employee
            self.__first_name = first
            self.__last_name = last
            self.__salary = rate
            self.__commission_rate = commission
            self.__weekly_dues = dues

    def set_employee(self, employee):
            self.__employee_id = employee

    def set_first(self, first):
            self.__first_name = first

    def set_last(self, last):
            self.__last_name = last

    def set_rate(self, rate):
            self.__salary = rate

    def set_commission(self, commission):
            self.__commission_rate = commission

    def set_dues(self, dues):
            self.__weekly_dues = dues

    def get_full_name(self):
            print("Employee: " + self.__last + ", " + self.__first)

