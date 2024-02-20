# Product Class

# Create a class called Product with the following private attributes: name, price, and quantity. 
# Implement getter and setter methods for each attribute. 
# Additionally, add a method to calculate the total value of the stock (price * quantity).

class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    # Getter methods
    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    # Setter methods
    def set_name(self, name):
        self._name = name

    def set_price(self, price):
        self._price = price

    def set_quantity(self, quantity):
        self._quantity = quantity

    # Calculate total value of stock
    def calculate_stock_value(self):
        return self._price * self._quantity

# Example usage
product1 = Product("iPhone 15", 1249.99, 50)
print(f"Product: {product1.get_name()}")
print(f"Price: {product1.get_price():.2f}€")
print(f"Quantity: {product1.get_quantity()}")
print(f"Total stock value: {product1.calculate_stock_value():.2f}€")
