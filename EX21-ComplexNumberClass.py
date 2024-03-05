# Complex Number Class

# Create a class called ComplexNumber that represents a complex number with real and imaginary parts. 
# The class should have attributes _real_part and _imaginary_part to store the real and imaginary parts, respectively. 
# Use properties to ensure that the real and imaginary parts can only be assigned with numerical values.

class ComplexNumber:
    def __init__(self, real_part: float, imaginary_part: float): # Initializes the real part and imaginary part attributes
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    @property
    def real_part(self):
        return self._real_part

    @real_part.setter
    def real_part(self, value):
        if isinstance(value, (int, float)): # Verifies if the assigned value is numeric
            self._real_part = value
        else:
            raise ValueError("The real part must be a numeric value.")

    @property
    def imaginary_part(self):
        return self._imaginary_part

    @imaginary_part.setter
    def imaginary_part(self, value):
        if isinstance(value, (int, float)):
            self._imaginary_part = value
        else:
            raise ValueError("The imaginary part must be a numeric value.")

    def __str__(self):
        # Special method to return a string representation of the complex number
        # Formats the imaginary part with the "i" symbol

        if self._real_part == 0 and self._imaginary_part != 0:
            return f"{self._imaginary_part}i"
        elif self._imaginary_part == 0:
            return f"{self._real_part}"
        else:
            sign = '+' if self._imaginary_part > 0 else ''
            return f"{self._real_part} {sign} {self._imaginary_part}i"


def get_numeric_value(message: str) -> float:
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Error: Please enter a valid numeric value.")


print("Enter the parts of the complex number:")
real_part = get_numeric_value("Real part: ")
imaginary_part = get_numeric_value("Imaginary part: ")
complex_number = ComplexNumber(real_part, imaginary_part)
print("Complex number:", complex_number)