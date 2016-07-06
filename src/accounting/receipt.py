class Receipt:
    def __init__(self, date, amt):
        self.__date = date
        self.__sale_amt = amt

    def get_receipt(self):
        stmt_str = "Invoice Number: {0}, Date: {1}, Amount: {2}"
        print(stmt_str.format(self.__invoice, self.__date, self.__sale_amt))
