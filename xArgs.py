# *args allows a function to accept a variable number of positional arguments.

def add(*numbers):
    total = 0
    for n in numbers:
        total += n
    print("Sum:", total)

add(10, 20)
add(1, 2, 3, 4)

