# Product Class **Unit Price Increase Exercise**

# Create a program that allows the updating of product prices whenever there is a percentage increase in the unit price. 
# To accomplish this, it will be necessary to use a class with the variable 'increase'.
# It will also be necessary the method to assign values to it so that it is possible to update the value of the products.

class Product:
    def __init__(self, description, quantity, unit_price):
        self._description = description
        self._quantity = quantity
        self._unit_price = unit_price
        self._increase = 0

    @staticmethod
    def increase_percentage(percentage):
        Product._increase = percentage

    @property
    def product_value(self):
        return self._quantity * self._unit_price * (1 + self._increase / 100)

    @staticmethod
    def print_header():
        print(f"{'Description':<15}{'Value (€)':>10}") # printing the header with formatted alignment


    def print_product(self):
        print(f"{self._description:<15} {self.product_value:^8.2f}")


def main():
    products = (('LP1', 100, 10), ('LP2', 200, 10), ('LP3', 150, 15)) # tuple of products
    percentage = 5
    Product.increase_percentage(percentage)
    Product.print_header()
    for p in products:
        pr = Product(*p) # "unpacking" operator - equivalent to Product(p[0], p[1], p[2]) 
        pr.print_product()


if __name__ == '__main__':
    main()
