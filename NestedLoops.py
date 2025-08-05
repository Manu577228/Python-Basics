# Nested loops are loops inside other loops. Inner loops run fully for each outer loop iteration.

for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")