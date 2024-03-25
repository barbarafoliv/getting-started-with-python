# Attribute Validation with Metaclass

# Create a metaclass that validates the attributes of a class.
# For example, the metaclass can ensure that all attributes of a class are strings.
# You should create classes with different types of attributes and observe how the validation works.

class AttributeValidationMeta(type):
    def __new__(cls, name, bases, dct):
        # Check if all attributes are strings
        for attr_name, attr_value in dct.items():
            if not isinstance(attr_value, str):
                raise TypeError(f"Attribute '{attr_name}' must be a string.")
        
        # Creating the class using type's __new__ method
        new_class = super().__new__(cls, name, bases, dct)
        return new_class

# Applying the metaclass to a base class
class Base(metaclass=AttributeValidationMeta):
    pass

# Example classes
class MyClass1(Base):
    name = 'John'
    age = 30  # This should be a string
    email = 'john@example.com'

class MyClass2(Base):
    city = 'New York'
    population = 1000000  # This should be a string

# Testing the classes
obj1 = MyClass1()
obj2 = MyClass2()
