# Coroutine that receives numbers and returns the cumulative average.

# Implement a coroutine in Python that receives numbers and returns the cumulative average.

# Asynchronous function, typically used for operations that may involve waiting for I/O operations or other asynchronous tasks
async def cumulative_average(): 
    total_sum = 0 # Total sum of numbers received
    count = 0 # Number of elements received
    
    # The coroutine will keep running indefinitely, continuously receiving numbers and calculating the cumulative average
    while True:
        number = await receive_number() # Use an infinite loop to continually receive numbers using the await keyword
        total_sum += number
        count += 1
        yield total_sum / count # Yield a value to its caller, suspending its state and later resuming execution from the same point

async def receive_number():
    # Simulating receiving numbers asynchronously
    number = float(input("Enter a number: "))
    return number

# Example usage:
async def main(): # This function serves as the entry point for executing the coroutine
    coroutine = cumulative_average()
    async for average in coroutine:
        print("Cumulative average:", average)

import asyncio # Provides infrastructure for writing single-threaded concurrent code using coroutines
asyncio.run(main())
