# Reduce

reduce applies a function with 2 arguments (func(arg1,arg2)) cumulatively to the elements of an iterable .

## syntax 
reduce (func,iterable[,initial])

## Example 

Provide sum of all elements in a list .

numbers = [1,2,3,4,5,6]

def add(x,y):
    return x+y

sum = reduce(add,numbers)

