"""
Exercise

Edit the function provided by calling partial() and replacing the first three variables in func(). 
Then print with the new partial function using only one input variable so that the output equals 60.
#Following is the exercise, function provided:

def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

"""

from functools import partial 

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

new_part = partial(func,4,3,2)

print(new_part(31))
