# Create a class Email that represents an email address.
# The class should have an attribute _address to store the email address.
# The class should have a method valid() that returns True if the email address is valid.
# Use a property to ensure that the email address contains either "@xyz.com" or "@xpto.pt".

class Email:
    def __init__(self, address):
        self._address = address
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address):
        if self.valid(new_address):
            self._address = new_address
        else:
            raise ValueError("Invalid email address")
    
    def valid(self, address):
        if "@xyz.com" in address or "@xpto.pt" in address:
            return True
        else:
            return False

# Usage example
def main():
    my_email = Email("example@xyz.com")
    print(my_email.valid(my_email.address))  # Output: True

    # Attempt to assign an invalid address
    try:
        my_email.address = "another@domain.com"
    except ValueError as e:
        print(e)  # Output: Invalid email address

if __name__=='__main__':
    main()
