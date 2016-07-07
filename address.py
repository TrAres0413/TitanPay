class Address:
    def __init__(self, street, city, state, zip_code):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip = zip_code

    def get_address(self):
        stmt_str = "Employee Address: Street- {0}, City- {1}, State- {2}, Zip- {3}"
        print(stmt_str.format(self.__street_address, self.__city, self.__state, self.__zip))
