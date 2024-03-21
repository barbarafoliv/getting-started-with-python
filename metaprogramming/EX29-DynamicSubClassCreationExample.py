# Define the initialization method for the base class
def init(self, language):
    """Initialize the language attribute."""
    self.language = language

# Define a method to get the language
def get_language(self):
    """Return the language attribute."""
    return self.language

# Define a function to return Python types
def py_types(self):  # Accept class parameter to make it a class method
    """Return a set containing common Python types."""
    return {'print', 'input'}

# Create the base class dynamically using type()
LanguagesType = type('LanguagesType', (object, ), {
    '__init__': init,
    'get_language': get_language,
})

# Create a subclass using type()
InstanceType = type('InstanceType', (LanguagesType, ), {
    'py_types': py_types,  
})

# Create an instance of the subclass
instance = InstanceType(language='Python')

# Access methods of the instance
print(instance.get_language())   # Output: Python
print(instance.py_types())       # Output: {'input', 'print'}



