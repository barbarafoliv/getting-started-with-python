# Triangle Class

# Implement a Triangle class with the attributes side1, side2 and side3. 
# Getters and setters must ensure that the values assigned to the sides are positive 
# and that the sum of any two sides is greater than the third (to ensure it is a valid triangle).

class Triangle:
    def __init__(self, initial_side1: float, initial_side2: float, initial_side3: float):
        self._side1 = max(0, initial_side1)
        self._side2 = max(0, initial_side2)
        self._side3 = max(0, initial_side3)

    def get_side1(self) -> float:
        return self._side1

    def get_side2(self) -> float:
        return self._side2

    def get_side3(self) -> float:
        return self._side3

    def set_side1(self, new_side1: float) -> None:
        if new_side1 > 0:
            self._side1 = new_side1

    def set_side2(self, new_side2: float) -> None:
        if new_side2 > 0:
            self._side2 = new_side2

    def set_side3(self, new_side3: float) -> None:
        if new_side3 > 0:
            self._side3 = new_side3

    def is_valid(self) -> bool: # The \ is essential to change line
        return self._side1 + self._side2 > self._side3 and \
               self._side1 + self._side3 > self._side2 and \
               self._side2 + self._side3 > self._side1

# Example usage
triangle = Triangle(3, 4, 5)
print(f"Is the triangle valid? {triangle.is_valid()}")
