# A list in Python is an ordered, mutable (changeable) collection that can hold items of any data type.
# Lists allow indexing, slicing, adding, removing, and updating elements.

# Adding : .append(), .insert(), +
# Removing : .pop(), .remove(), del
# Accessing: [i], slicing [i:j]
# Modifying: list[i] = value

my_list = [10, "Hello", 3.14, True]
print("Original List:", my_list)

print("First element:", my_list[0])
print("Last element:", my_list[-1])

print("Slice [1:3]:", my_list[1:3])

my_list.append("World")
print("After append:", my_list)

my_list.insert(1, 99)
print("After Insertion:", my_list)

my_list.pop()
print("After pop:", my_list)

my_list.remove(99)
print("After removal of 99:", my_list)

my_list[0] = 100
print("After modifying first element:", my_list)




