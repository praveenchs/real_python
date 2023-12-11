""" Exercise
Write a generator function which returns the Fibonacci series. They are calculated using the following formula: The first two numbers of the series is always equal to 1, and each consecutive number returned is the sum of the last two numbers.
Hint: Can you use only two variables in the generator function? Remember that assignments can be done simultaneously. 
The code
"""

def fib(x):
    a = 0
    b = 1
    
    yield b

    for i in range(x):
        yield a+b
        a , b = b , a+b #  It utilizes tuple packing and unpacking to make the code more concise and readable.
        
        ṇ


""" for number in fib(9):
    print(number) """
fib_list = list(fib(20)) # to retrieve values with a generator function , you need an iterable operation (for loop or list) .
print(fib_list) # Then you need to print the list 



    

