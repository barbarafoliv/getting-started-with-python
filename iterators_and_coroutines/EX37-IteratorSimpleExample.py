# List of fruits
fruits = ['apples', 'pears', 'oranges', 'peaches', 'watermelon']
fruits_iteration = iter(fruits)

print(next(fruits_iteration), -1) # When iterator reaches its limit, present the alternative value = -1.
print(next(fruits_iteration))
print(next(fruits_iteration))  # The fruits peaches and watermelon are not iterated

"""
Output:
apples
pears
oranges

Each time the statement print(next(fruits_iteration)) is used, it performs one more iteration in the list up to the maximum the list 
contains. The first iteration always starts from the first position of the list, i.e., position 0, and subsequent iterations go up to the 
maximum of the list. If the positions exceed the size of the list, an error message will be obtained.
"""

