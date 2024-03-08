from Property import *

class Apartment(Property):
    def __init__(self, owner, fiscal_number, type, area):
        super().__init__(owner, fiscal_number)
        self.__type = type
        self.__area = area
        
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type
        
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, area):
        self.__area = area
