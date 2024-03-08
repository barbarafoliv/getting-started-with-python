# Email Class

# Create a class Email that represents an email address. 
# The class should have an attribute _address to store the email address.
# The class should have a method valid() that returns True if the email address is valid. 
# Use a property to ensure that the email address contains an '@'.

class Email:
    def __init__(self, address):
        self._address = address
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address):
        if ("@" in new_address) and ((".com" in new_address ) or (".pt" in new_address)):
            self._address = new_address
        else:
            print("Invalid email address. It should contain '@' and end with \".com\" or \".pt\".\n")
    
    def is_valid(self):
        return ("@" in self._address ) and ((".com" in self._address ) or (".pt" in self._address))
    
    def print_info(self):
        print(f"\nThe email address is: {self._address} \n")


if __name__ == "__main__":
    # Create the Email object
    my_email = Email("formando@dual.pt") # Output: formando@dual.pt

    # Print the defined email
    print("\n\n\n" + my_email.address + "\n") 

    # Verify if the email address is valid
    print(f"Is the email valid? {my_email.is_valid()}\n\n")  # Output: True

    # Try to set an invalid email address
    print(f"Change the email test 1: \n")  # Output: If invalid prints error message
    my_email.address = "email_sem-o-arroba.com"  # Output: Invalid email address. It should contain '@' and end with ".com" ou ".pt".

    # Try to set an invalid email address
    print(f"Change the email test 2: \n")  # Output: If invalid prints error message
    my_email.address = "email@example"  # Output: Invalid email address. It should contain '@' and end with ".com" ou ".pt".

    # Try to set an invalid email address
    print(f"Change the email test 3: \n\n")  # Output: If invalid prints error message
    my_email.address = "formador@dual.com"  # Output: Valid. No error message in printed. 

    # Verify that email was changed
    print("\nEmail address: " + my_email.address + "\n\n\n") # Output: formador@dual.com
    
    chosen_email = Email(input("Enter the email: "))
    
    while True:
        print("\nChoose an option:")
        print("1 - Change email")
        print("2 - More info")
        print("3 - Exit")

        choice = input("Option: ")

        if choice == '1':
            new_email = input("Enter a new email: ")
            chosen_email.address = new_email
        elif choice == '2':
            chosen_email.print_info()
        elif choice == '3':
            print("\nSee you next time!\n")
            break
        else:
            print("Invalid option. Please choose a valid option.\n")