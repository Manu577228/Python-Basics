# Searching refers to finding the presence or position of a particular element in a collection (like lists, tuples, sets).
# Python supports linear search and Binary Search we can use the in keyword or .index() method for common operations.

# bisect module -> Binary Search

data = [10, 25, 30, 45, 60]

if 30 in data:
    print("30 is present in the list")

position = data.index(45)
print("Position of 45:", position)

try:
    print("Position of 99:", data.index(99))
except ValueError:
    print("99 is not present in the list")

import bisect
i = bisect.bisect_left(data, 45)
if i < len(data) and data[i] == 45:
    print("Found 45 using Binary Search at index:", i)
else:
    print("45 not found")






