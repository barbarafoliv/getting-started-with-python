# Define the Property class, and the subclasses House and Apartment that derive from Property

class Property:
    def __init__(self, owner_name, fiscal_number):
        self.__owner = owner_name
        self.__fiscal_number = fiscal_number
        
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, name):
        self.__owner = name
        
    @property
    def fiscal_number(self):
        return self.__fiscal_number
    
    @fiscal_number.setter
    def fiscal_number(self, number):
        self.__fiscal_number = number
