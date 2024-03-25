# Creating an Attribute Count Metaclass

# Create a metaclass that counts the number of attributes in a class.
# When creating a new class, the metaclass should print the number of attributes the class has.
# You should create several classes and observe how the attribute count varies.

class AttributeCountMeta(type):
    def __new__(cls, name, bases, dct):
        # Counting the number of attributes
        attribute_count = len(dct)
        # Creating the class using type's __new__ method
        new_class = super().__new__(cls, name, bases, dct)
        # Printing the count of attributes
        print(f"Class '{name}' has {attribute_count} attributes.")
        return new_class

# Applying the metaclass to a base class
class Base(metaclass=AttributeCountMeta):
    pass

# Example classes
class MyClass1(Base):
    x = 10
    y = 20

class MyClass2(Base):
    a = 'apple'
    b = 'banana'
    c = 'cherry'
    d = 'date'

class MyClass3(Base):
    foo = 'bar'
    spam = 'eggs'
    baz = 'qux'
    extra_attribute = 'extra'

# Testing the classes
obj1 = MyClass1()
obj2 = MyClass2()
obj3 = MyClass3()
