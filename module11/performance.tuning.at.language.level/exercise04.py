"""
Pick/Design right data structure
append/pop at the end -> list
appending/pop at the beginning -> collections.deque
...
"""
from collections import deque

numbers = [] #list
numbers2 = set() #set
number = 42
if number in numbers: # O(n)
    print("found")
for number in numbers:
    print(number)
sum(numbers)

numbers = deque(numbers)
numbers.append(42)
numbers.insert(0,42) # worst scenario

