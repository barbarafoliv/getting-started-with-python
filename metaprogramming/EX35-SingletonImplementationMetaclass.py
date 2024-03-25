# Implementing a Singleton with Metaclass

# Implement a Singleton using a metaclass.
# The Singleton should ensure that only one instance of the class is created. 
# You should create multiple instances of the class and verify if they are all equal.

class SingletonMeta(type):
    _instances = {} # This dictionary will store instances of classes that use SingletonMeta as their metaclass.

    # It's overridden to control the instantiation process of classes that use SingletonMeta as their metaclass.
    def __call__(cls, *args, **kwargs): 
        # Checks if the class (cls) is already in the _instances dictionary. If not, no instance of this class has been created yet.
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# Applying the metaclass to a base class
class Singleton(metaclass=SingletonMeta):
    pass

# Example usage
class MyClass(Singleton):
    def __init__(self, value):
        self.value = value

# Creating instances and checking if they are equal
instance1 = MyClass(10)
instance2 = MyClass(20)
instance3 = MyClass(30)

print(instance1.value)  # Output: 10
print(instance2.value)  # Output: 10
print(instance3.value)  # Output: 10

print(instance1 is instance2 is instance3)  # Output: True
