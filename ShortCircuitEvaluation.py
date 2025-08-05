# In Python, logical operators use short-circuit evaluation, 
# where it stops evaluating as soon as the result is determined.

def check():
    print("check() called")
    return True

print(False and check())
print(True or check())
print(True and check())



