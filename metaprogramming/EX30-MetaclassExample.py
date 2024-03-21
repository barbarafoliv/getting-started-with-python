class MetaClass(type):
    """Example of a metaclass without functionality"""
    # Define the __new__ method, which is called when a new class object is created
    def __new__(cls, class_name, superclasses, attribute_dict):
        # Print the name of the class being created
        print("class_name:", class_name)
        # Print the superclasses of the class being created
        print("superclasses:", superclasses)
        # Print the attributes (methods and properties) of the class being created
        print("attribute_dict:", attribute_dict)
        # Call the __new__ method of the superclass (type) to create the class object
        return super(MetaClass, cls).__new__(cls, class_name, superclasses, attribute_dict)

# Create an instance of the MetaClass metaclass, effectively creating a new class named 'C'
C = MetaClass('C', (object, ), {})

# Print the type of the newly created class 'C'
print("type of class:", type(C))

