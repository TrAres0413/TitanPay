

class PaymentMethod:
    def __init__(self, employee_id):
        self.__employee = employee_id

    def pay(self, amt):
        print("Paying Amount", amt)


