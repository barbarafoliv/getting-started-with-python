# Date Class

# Create a class Date that represents a date with day, month, and year.
# Use properties to ensure that the day is within the valid range for the provided month and year.

def main():
    date = Date() # Instantiates an object from class Date
    date.insert_date() # Asks the user to enter a date
    print("The date is:", date.day, "/", date.month, "/", date.year) # Shows the entered date


class Date:
    def __init__(self): # Attributes are initialized as None (same as "Null")
        self._day = None
        self._month = None
        self._year = None

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, new_day):
        if self._is_valid_date(new_day, self._month, self._year):
            self._day = new_day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, new_month):
        if self._is_valid_date(self._day, new_month, self._year):
            self._month = new_month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        self._year = new_year 


    def _is_valid_date(self, day, month, year):
        if month < 1 or month > 12: # Invalid month
            return False
        
        if day < 1: # Invalid day
            return False
        
        if month == 2:
            if self._is_leap_year(year):
                return day <= 29
            else:
                return day <= 28
            
        if month in {4, 6, 9, 11}:
            return day <= 30
        else:
            return day <= 31
    
    def _is_leap_year(self, year): # Case in which the year has 366 days
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False
    
    def insert_date(self):
        while True:
            try:
                day = int(input("Enter the day: "))
                month = int(input("Enter the month: "))
                year = int(input("Enter the year: "))

                if self._is_valid_date(day, month, year):
                    self._day = day
                    self._month = month
                    self._year = year
                    break
                else:
                    print("Error: Invalid date. Please enter a valid date.")
            except ValueError:
                print("Error: Enter numeric values for day, month and year.")


if __name__ == '__main__':
    main()