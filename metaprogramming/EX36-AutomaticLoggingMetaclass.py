# Automatic Logging

# The LogMeta metaclass is created to automatically register all method calls of a class in a log file. 
# Within the __new__ method, all methods of the class are decorated with a wrapper that logs the method call to the log file.

import logging

# Configuring logging
logging.basicConfig(filename='method_calls.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class LogMeta(type): # Define the metaclass to add automatic logging to the class methods
    def __new__(cls, name, bases, dct):
        # Decorating all methods with a wrapper that logs method calls
        for attr_name, attr_value in dct.items(): # Iterate over the class attributes
            if callable(attr_value): # Check if the attribute is a method (callable)
                dct[attr_name] = cls.log_method_call(attr_value) # If it's a method, decorate it with the logging wrapper 
        return super().__new__(cls, name, bases, dct) # Create the class with decorated methods

    @staticmethod
    def log_method_call(method):
        def wrapper(*args, **kwargs):
            logging.info(f"Method '{method.__name__}' called with args: {args}, kwargs: {kwargs}")
            return method(*args, **kwargs)
        return wrapper

# Applying the metaclass to a base class
class LoggedClass(metaclass=LogMeta):
    pass

# Example class
class MyClass(LoggedClass):
    def __init__(self, value):
        self.value = value

    def double_value(self):
        return self.value * 2

# Creating an instance and calling a method
obj = MyClass(5)
result = obj.double_value()  # This method call will be logged
print(result)  # Output: 10

'''
This code creates a metaclass named LogMeta that automatically decorates all methods of a class with a wrapper that logs the method calls 
into a log file. Then, the class MyClass is defined with this metaclass, which means that all methods of this class will be automatically 
decorated with the logging functionality. When creating an instance of MyClass and calling its methods, the method calls are logged into a 
log file named "method_calls.log".
'''
