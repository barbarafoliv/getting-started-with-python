# Temperature Class - **Upgraded**

# Define the class "Temperature" with two instance variables, C and F.
# C and F represent a certain temperature in Celsius and Fahrenheit degrees, respectively. 
# Elaborate a test program that reads the temperature in Celsius degrees and converts it to Fahrenheit degrees. 
# Fahrenheit degrees = 1.8 * Celsius degrees + 32

class Temperature:
    def __init__(self, celsius):
        self.C = celsius
        self.F = self.convert_to_fahrenheit(celsius)

    @staticmethod
    def convert_to_fahrenheit(celsius):
        return 1.8 * celsius + 32
    
    def readC(self):
        return f"{self.C:>2.1f}"
    
    def readF(self):
        return f"{self.F:<2.1f}"
    
    def printTemperature(self):
        print(f"{self.readC()} C = {self.readF()} F")

if __name__=='__main__':
    Temp=float(input("Enter the temperature in Celsius: "))
    T=Temperature(Temp)
    T.printTemperature()
