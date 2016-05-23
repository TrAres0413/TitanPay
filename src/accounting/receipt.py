class Receipt:
    def __init__(self, date, amt):
        self.__date = date
        self.__sale_amt = amt

    def set_date(self, date):
        self.__date = date

    def set_sale_amt(self, amt):
        self.__sale_amt = amt
