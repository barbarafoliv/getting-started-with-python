# Book Class

# Create a class Book that represents a book with title, author, and number of pages. 
# Use properties to ensure that the title and author are strings and the number of pages is a positive integer.

class Book:
    def __init__(self, title, author, num_pages):
        self._title = title
        self._author = author
        self._num_pages = num_pages

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise ValueError("Title must be a string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value
        else:
            raise ValueError("Author must be a string")

    @property
    def num_pages(self):
        return self._num_pages

    @num_pages.setter
    def num_pages(self, value):
        if isinstance(value, int) and value > 0:
            self._num_pages = value
        else:
            raise ValueError("Number of pages must be a positive integer")

# Example usage:
book1 = Book("Harry Potter", "J.K. Rowling", 300)
print(book1.title)  # Output: Harry Potter
print(book1.author)  # Output: J.K. Rowling
print(book1.num_pages)  # Output: 300

# Trying to set invalid values
try:
    book1.title = 123
except ValueError as e:
    print(e)  # Output: Title must be a string

try:
    book1.num_pages = -50
except ValueError as e:
    print(e)  # Output: Number of pages must be a positive integer
