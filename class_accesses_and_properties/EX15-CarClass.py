# Car Class

# Create a Car class with the attributes make, model, year and mileage. 
# Implement getters and setters for each attribute. 
# Ensure that the year is a positive value and that the mileage is not negative.

class Car:
    def __init__(self, make: str, model: str, year: int, mileage: float):
        self._make = make
        self._model = model
        self._year = max(0, year)  # Ensure positive year
        self._mileage = max(0, mileage)  # Ensure non-negative mileage

    def get_make(self) -> str:
        return self._make

    def get_model(self) -> str:
        return self._model

    def get_year(self) -> int:
        return self._year

    def get_mileage(self) -> float:
        return self._mileage

    def set_make(self, new_make: str) -> None:
        self._make = new_make

    def set_model(self, new_model: str) -> None:
        self._model = new_model

    def set_year(self, new_year: int) -> None:
        if new_year > 0:
            self._year = new_year

    def set_mileage(self, new_mileage: float) -> None:
        if new_mileage >= 0:
            self._mileage = new_mileage

# Example usage
car = Car(make="Toyota", model="Camry", year=2022, mileage=15000)
print(f"Car details: {car.get_make()} {car.get_model()}, Year: {car.get_year()}, Mileage: {car.get_mileage()} km")
car.set_year(2023)
car.set_mileage(16000)
print(f"Updated year: {car.get_year()}, Updated mileage: {car.get_mileage()} km")
