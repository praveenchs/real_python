"""
*** Partial Functions ***

Partial functions are created by reusing a function/method , with some fixed arguments. 
Its best understood with an example .

we create a function called "power" , which accepts 2 arguments - base and exponent

Now we write a partial function called square = where the exponent is fixed to 2 , allows arguments only for base .



Partial Functions are available as part of functools library ..

"""
from functools import partial

def Power(base,exponent):
    return base ** exponent

# create partial function called square

Square = partial(Power,exponent=2)

# We can call this partial function by providing single argument

print(Square(3))
    

# Create a partial function called cube , which provides cube for the given base number

cube = partial(Power,exponent=3)

print(cube(4))
