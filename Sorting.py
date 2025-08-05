# Sorting is the process of arranging data in a particular order (ascending or descending).
# Python offers built-in methods like sorted() and .sort() for sorting iterable objects.

numbers = [5, 2, 9, 1, 7]

sorted_numbers = sorted(numbers)
print("Sorted list (ascending):", sorted_numbers)

desc_numbers = sorted(numbers, reverse=True)
print("Sorted list (descending):", desc_numbers)

print("Original list:", numbers)

numbers.sort()
print("List after in-place sort:", numbers)





