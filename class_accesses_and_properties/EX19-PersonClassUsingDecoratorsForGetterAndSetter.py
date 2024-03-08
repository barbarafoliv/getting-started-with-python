# Person Class

class Person:
    def __init__(self):
        self._name = None # Protected attribute starting with '_' to indicate it is private
        self.__original_name = None # Private attribute to store the original name

    # Method to get the original name
    def get_original_name(self):
        return self.__original_name

    # Getter for the name attribute
    @property 
    def name(self):
        return self._name

    # Setter for the name attribute
    @name.setter 
    def name(self, new_name):
        # Store the original value before changing it, but only if it hasn't been stored yet
        if self.__original_name is None:
            self.__original_name = self._name

        # Update the name attribute with the new value
        self._name = new_name
        
        # Print a message indicating that the name was changed and show the old and new values
        print(f"The name was changed from '{self.__original_name}' to '{new_name}'")


# Example of use
if __name__ == "__main__":
    # Creation of a Person object
    person = Person()
    print("Person's name:", person.name)

    # Using the setter to assign a value to the name
    person.name = "John"

    # Using the getter to get the name value and print
    print("Person's name:", person.name)

    # Using the setter to change the name value
    person.name = "Mary"

    # Using the getter again to get the new name value and print
    print("New name of the person:", person.name)

    # Getting the original name value before the last change
    original_name = person.get_original_name()

    # Printing the original name value
    print("Original name value:", original_name)
