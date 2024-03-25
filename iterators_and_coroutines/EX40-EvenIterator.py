# Iterator to traverse a list of numbers and return only the even numbers

# Create a class EvenIterator that implements an iterator to traverse a list of numbers and return only the even numbers.

"""
To solve this exercise in Python, I followed these steps:

1. Define a class named EvenIterator.
2. Implement the __init__() method to initialize the iterator with the list of numbers.
3. Implement the __iter__() method to return the iterator object.
4. Implement the __next__() method to return the next even number in the list, and raise a StopIteration exception when there are no more even numbers.
5. Test the iterator by iterating over it and printing the even numbers.
"""

class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.numbers):
            if self.numbers[self.index] % 2 == 0:
                result = self.numbers[self.index]
                self.index += 1
                return result
            else:
                self.index += 1
        raise StopIteration

# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_iter = EvenIterator(numbers_list)

for num in even_iter:
    print(num)
