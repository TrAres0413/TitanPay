

class Employee:
    def __init__(self, employee_id, first, last, dues, pay_method):
        self.__employee_id = employee_id
        self.__first_name = first
        self.__last_name = last
        self.__weekly_dues = dues
        self.__pay_method = pay_method

    def set_employee(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def set_first(self, first):
        self.__first_name = first

    def get_first_name(self):
        return self.__first_name

    def set_last(self, last):
        self.__last_name = last

    def get_last_name(self):
        return self.__last_name

    def set_dues(self, dues):
        self.__weekly_dues = dues

    def get_dues(self):
        return self.__weekly_dues

    def set_pay_method(self, pay_method):
        self.__pay_method = pay_method

    def get_full_name(self):
        return "Employee: " + self.__last_name + ", " + self.__first_name

    def get_payment_method(self):
        return self.__pay_method
