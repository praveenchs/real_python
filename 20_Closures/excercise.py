"""
Exercise

Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures. 
That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.
"""

"""multiplywith5 = multiplier_of(5)
multiplywith5(9)"""


def multiplier_of(number): # pass variable =5 to the function
    # This is nested function
    print("enclosed variable :", number)
    def multiply_with(numb):
        print("nested variable :" , numb)
        return number * numb
    # call the nested function
    return multiply_with

multiplywith5 = multiplier_of(5)
print(multiplywith5(9))





    