class Receipt:
    def __init__(self, date, amt, invoice):
        self.__date = date
        self.__sale_amt = amt
        self.__invoice = invoice

    def set_invoice(self, invoice):
        self.__invoice = invoice

    def set_date(self, date):
        self.__date = date

    def set_sale_amt(self, amt):
        self.__sale_amt = amt

    def get_receipt(self, invoice):
        stmt_str = "Invoice Number: {0}, Date: {1}, Amount: {2}"
        print(stmt_str.format(self.__invoice, self.__date, self.__sale_amt))
