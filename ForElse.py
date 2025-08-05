# The else block in a for loop runs only if the loop completes without break.

for i in range(5):
    if i == 7:
        break
    print(i)
else:
    print("Loop Completed")