from Person import *

class Friend(Person):
    def __init__(self, name, phone, location, year):
        super().__init__(name, phone)
        self._location = location
        self._year = year

    def get_location(self):
        return self._location

    def get_year(self):
        return self._year

    def print_friend_details(self):
        super().print_details()
        print(f" -- {self._location} -- {self._year}")
