# Circumference Class

# Implement a Circumference class with the radius attribute. 
# Getters and setters must ensure that the radius is a positive value. 
# Add a method to calculate the area of a circle.

import math

class Circumference:
    def __init__(self, radius: float):
        self._radius = max(0, radius)  # Ensure positive radius

    def get_radius(self) -> float:
        return self._radius

    def set_radius(self, new_radius: float) -> None:
        if new_radius > 0:
            self._radius = new_radius

    def calculate_area(self) -> float:
        return math.pi * self._radius ** 2

# Example usage
circle = Circumference(radius=5)
print(f"Radius: {circle.get_radius()}")
print(f"Area of the circle: {circle.calculate_area():.2f} square units")
