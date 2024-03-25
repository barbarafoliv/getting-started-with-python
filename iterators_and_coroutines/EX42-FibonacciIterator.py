# Implementation of an iterator that returns Fibonacci numbers

# Develop a class FibonacciIterator that implements an iterator to return Fibonacci numbers up to a maximum value.

class FibonacciIterator:
    def __init__(self, max_value): # Initializes the iterator with the maximum value up to which Fibonacci numbers should be generated
        self.max_value = max_value
        self.prev, self.curr = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr > self.max_value:
            raise StopIteration
        else: # Calculates and returns the next Fibonacci number in the sequence until it exceeds the maximum value specified
            result = self.curr
            self.prev, self.curr = self.curr, self.prev + self.curr
            return result

# Example usage:
max_value = 1000
fibonacci_iter = FibonacciIterator(max_value)

for num in fibonacci_iter:
    print(num)
