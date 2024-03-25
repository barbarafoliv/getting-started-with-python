# In the following example, we do not implement a StopIteration condition. 
# Instead, we use the iter() method with a sentinel parameter to stop the iteration:
# my_iter = iter(DoubleIt(), 16)
# The value of the sentinel parameter will be 16.
# This will cause the program to stop iterations when the value of the __next__() method equals this number.
# At this point in the code, the program will automatically raise a StopIteration.

class DoubleIt:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.num *= 2
        return self.num
    
    __call__=__next__

# Example usage:
my_iter = iter(DoubleIt(), 16)

for num in my_iter:
    print(num)
