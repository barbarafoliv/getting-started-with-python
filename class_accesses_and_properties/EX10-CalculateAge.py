# Calculate Age

import datetime

class Person:
    def __init__(self, birthday):
        self._birthday = birthday

    def calculate_age(self):
        current_date = datetime.date.today()
        age = current_date.year - self._birthday.year - ((current_date.month, current_date.day) < (self._birthday.month, self._birthday.day))
        return age

if __name__ == "__main__":
    birthday = datetime.date(1991, 7, 30)
    myself = Person(birthday)
    print(f"I'm {myself.calculate_age()} years old.")
