# Rectangle Class

# Create a Rectangle class that represents a rectangle with width and height. 
# Use properties to ensure that the width and height are positive numbers.

class Rectangle:
    """
    A class used to represent a Rectangle.
    """
    def __init__(self, width: float, height: float):
        """
        Initialize the Rectangle with the specified width and height.
        Raises a ValueError if the width or height is less than or equal to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        """
        Return the width of the Rectangle.
        """
        return self._width

    @width.setter
    def width(self, value: float):
        """
        Set the width of the Rectangle.
        Raises a ValueError if the width is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError("Width must be a positive number")
        self._width = value

    @property
    def height(self) -> float:
        """
        Return the height of the Rectangle.
        """
        return self._height

    @height.setter
    def height(self, value: float):
        """
        Set the height of the Rectangle.
        Raises a ValueError if the height is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError("Height must be a positive number")
        self._height = value

    def area(self) -> float:
        """
        Return the area of the Rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Return the perimeter of the Rectangle.
        """
        return 2 * (self.width + self.height)
    

# Example usage:
try:
    rect = Rectangle(5, 10)
    print("Area:", rect.area())
    print("Perimeter:", rect.perimeter())
except ValueError as e:
    print(e) 
