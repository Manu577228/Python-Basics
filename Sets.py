# A set in Python is an unordered collection of unique and immutable elements.
# Sets are commonly used to eliminate duplicates and perform mathematical set operations.

#  {} or set()

# Union set1 | set2
# Intersection set1 & set2
# Difference set1 - set2
# Membership test: x in set

s = {1, 2, 3, 2, 1}
print("Set after creation:", s)

s.add(4)
print("After adding 4:", s)

s.remove(2)
print("After removing 2:", s)

print("IS 3 in Set?", 3 in s)
print("Is 5 in Set?", 5 in s)

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference", a - b)


