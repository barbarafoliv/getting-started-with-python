# Person Class

# Create a Person class with the attributes name, age and height. 
# Implement getters and setters for each attribute. 
# Make sure age and height cannot be negative values.

class Person:
    def __init__(self, initial_name: str, initial_age: int, initial_height: float):
        self._name = initial_name
        self._age = max(0, initial_age)  # Ensure non-negative age
        self._height = max(0, initial_height)  # Ensure non-negative height

    # Using distinct parameter names in the constructor ensures that the initial values are not 
    # accidentally overwritten by setter methods. 

    # Getter methods
    def get_name(self) -> str: # -> str is the return type of the function
        return self._name

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    # Setter methods
    def set_name(self, new_name: str) -> None: # None is the same as Void
        self._name = new_name

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height

# Example usage
person = Person(initial_name="Babi", initial_age=32, initial_height=1.73)
print(f"Name: {person.get_name()}, Age: {person.get_age()}, Height: {person.get_height()} m")
person.set_age(33)
person.set_height(1.72)
print(f"Updated Age: {person.get_age()}, Updated Height: {person.get_height()} m")
