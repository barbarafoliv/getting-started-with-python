# In the following example, we print the numbers from the iterator 1, 2, 3 using the __iter__() and __next__() methods.
# In this case, the __next()__ method has a loop that is executed until self.num is greater than or equal to self.max.
# Since we pass 3 as a parameter to the PrintNumber() object, self.max is initialized as 3. Therefore, the loop stops at 3.
# When self.num reaches the value of self.max, which is 3, the next() method raises a StopIteration exception.

class PrintNumber:
    def __init__(self, max):
        self.max = max
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.max:
            num = self.num
            self.num += 1
            return num
        else:
            raise StopIteration

# Example usage:
numbers = PrintNumber(3)
iterator = iter(numbers)

try:
    while True:
        print(next(iterator))
except StopIteration:
    pass
