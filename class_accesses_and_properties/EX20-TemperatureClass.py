# Temperature Class

# Create a Temperature class that represents a temperature in Celsius. 
# The class should have an attribute _celsius to store the temperature value in degrees Celsius. 
# Use properties to ensure that the temperature cannot be lower than absolute zero (-273.15°C).

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Temperature cannot be less than absolute zero (-273.15°C). Please enter a valid temperature.")
        else:
            self._celsius = value

    @classmethod # bound to the class and not the instance of the class
    def create_temperature(cls): # 1st argument to a class method is always a reference to the class itself - commonly named cls
        while True:
            try:
                celsius=float(input("Enter the temperature in Celsius:"))
                return cls(celsius)
            except ValueError:
                print("Please introduce a valid value for the temperature.")

if __name__ == "__main__":
    temperature = Temperature.create_temperature()
    print("Temperature in Celsius:", temperature.celsius)
