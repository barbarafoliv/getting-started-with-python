from Property import *

class House(Property):
    def __init__(self, owner, fiscal_number, location, category):
        super().__init__(owner, fiscal_number)
        self.__location = location
        self.__category = category
        
    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, location):
        self.__location = location
        
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, category):
        self.__category = category
