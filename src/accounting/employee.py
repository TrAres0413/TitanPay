class Employee:
    def __init__(self, employee_id, first, last, dues):
        self.__employee_id = employee_id
        self.__first_name = first
        self.__last_name = last
        self.__weekly_dues = dues

    def set_employee(self, employee_id):
        self.__employee_id = employee_id

    def set_first(self, first):
        self.__first_name = first

    def set_last(self, last):
        self.__last_name = last

    def set_dues(self, dues):
        self.__weekly_dues = dues

    def get_full_name(self):
        print("Employee: " + self.__last_name + ", " + self.__first_name)
