"""
*** Lambda Functions ***

Functions are defined once and we call it whenever we need to use it

What if a Function needs to be created for a one time use , enter Lambda Functions

"""

# Typical Function

def sum(a,b):
    return a+b

print(sum(3,5))

# Lambda FUnctions
# Syntax : your_function_name = lambda inputs : output

sum = lambda x,y : x+y
print(sum(30,5))
