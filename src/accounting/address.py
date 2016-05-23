class Address:
    def __init__(self, street, city, state, zip_code):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip = zip_code

    def set_street_address(self, street):
        self.__street_address = street

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip(self, zip_code):
        self.__zip = zip_code

    def get_address(self, street, city, state, zip_code):
        print("Employee Address: " + street + city + ", " + state + ". " + zip_code)