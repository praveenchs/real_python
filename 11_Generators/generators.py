# Generators

"""Generators are very easy to implement, but a bit difficult to understand.

Generators are used to create iterators, but with a different approach. 
Generators are simple functions which return an iterable set of items, one at a time, in a special way."""

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1,40)
    
    # returns a 7th number between 41 and 70
    yield random.randint(41,43)

for random_number in lottery():
    print(random_number)
