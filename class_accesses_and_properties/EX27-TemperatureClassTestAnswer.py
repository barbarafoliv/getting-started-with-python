# It is intended to define the Temperature class with two instance variables, C and F.
# C and F represent a certain temperature in degrees Celsius and degrees Fahrenheit.
# Also, elaborate a test program that reads the temperature in degrees Celsius and converts it to degrees Fahrenheit. 
# Fahrenheit = 1.8 * Celsius + 32

class Temperature:
    def __init__(self, celsius):
        self._C = celsius
        self._F = self.celsius_to_fahrenheit(celsius)

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, new_temperature):
        self._C = new_temperature

    @property
    def F(self):
        return self._F

    @F.setter
    def F(self, new_temperature):
        self._F = new_temperature

    def celsius_to_fahrenheit(self, celsius):
        return 1.8 * celsius + 32

    def print_temperature_in_fahrenheit(self):
        print(f"The temperature in Fahrenheit is: {self.F:.1f}°F")
        

# Test example
def main():
    celsius = float(input("Enter the temperature in Celsius: "))
    temperature = Temperature(celsius)
    temperature.print_temperature_in_fahrenheit()
    
    new_temperature = float(input("Enter a new temperature in Celsius: "))
    temperature.C = new_temperature
    temperature.F = temperature.celsius_to_fahrenheit(new_temperature)
    temperature.print_temperature_in_fahrenheit()

if __name__ == "__main__":
    main()
