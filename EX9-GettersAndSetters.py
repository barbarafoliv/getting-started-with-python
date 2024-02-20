# Getters and Setters

class Car:
    def __init__(self, color):
        self._color = color  # Private attribute with an underscore at the beginning

    # Getter to retrieve the car's color
    def get_color(self):
        return self._color

    # Setter to set the car's color
    def set_color(self, new_color):
        self._color = new_color

# Example usage
my_car = Car(color="red")
print("Car color:", my_car.get_color())  # Get the current color
my_car.set_color("blue")  # Set a new color
print("New car color:", my_car.get_color())  # Get the updated color


