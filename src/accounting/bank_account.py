class BankAccount:
    def __init__(self, bank, routing, account):
        self.__bank_name = bank
        self.__routing_number = routing
        self.__account_id = account

    def deposit(self, amt):
        stmt_str = "Depositing ${0} in Account: {1}, via Routing: {2}"
        print(stmt_str.format(amt, self.__account_id, self.__routing_number))

