from House import *
from Apartment import *

if __name__=='__main__':
    house=House("José Alves", "147098123", "Porto", "B")
    apartment=Apartment("Adelina Costa", "123567890", "T3", "200")

    print(house.owner, house.fiscal_number, house.location, house.category)
    print(apartment.owner, apartment.fiscal_number, apartment.type, apartment.area)