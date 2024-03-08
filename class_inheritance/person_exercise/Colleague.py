from Person import *

class Colleague(Person):
    def __init__(self, name, phone, profession, workplace):
        super().__init__(name, phone)
        self._profession = profession
        self._workplace = workplace

    def get_profession(self):
        return self._profession

    def get_workplace(self):
        return self._workplace

    def print_colleague_details(self):
        super().print_details()
        print(f" -- {self._profession} -- {self._workplace}")