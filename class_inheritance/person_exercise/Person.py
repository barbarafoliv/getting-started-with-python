class Person:
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def print_details(self):
        print(f"{self._name} -- {self._phone}", end="")