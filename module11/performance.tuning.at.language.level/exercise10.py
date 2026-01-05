# loops
from collections import deque

numbers = deque()
for number in numbers:  # faster and cleaner when compared to while
    print(number)

area_codes = {
    "istanbul-anadolu": 216,
    "istanbul-avrupa": 212,
    "ankara": 312
}

for city, number in area_codes.items():
    print(city, number)

for i, number in enumerate(numbers):
    print(i, number)
xs = []
ys = []
for x, y in zip(xs, ys):
    print(x, y)
