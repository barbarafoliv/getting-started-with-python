class MetaClass(type):
    """Example of constructing a metaclass"""
    def __new__(cls, class_name, superclasses, attribute_dict):
        # The __new__ method is called when a new class is created
        # It is responsible for creating the class and returning it
        # Here, we are using the __new__ method of the superclass (type) to create the class
        return super(MetaClass, cls).__new__(cls, class_name, superclasses, attribute_dict)

# Creating an instance of the MetaClass metaclass, which creates a class
C = MetaClass('C', (object, ), {})

# Defining a class A that inherits from class C, which was created with the MetaClass metaclass
class A(C):
    pass

# Printing the type of class A
print(type(A)) # Class A is an instance of a metaclass. This occurs because its superclass C is an instance of a metaclass.
