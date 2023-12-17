""" 
*** Exception Handling ***

When Python or any programming language gets an error , due to  various reasons :
    wrong user input or the 
    system was out memory 

Exception handling allows you to manage these errors like by logging the error message 


"""

# below error indicates that the variable "a" is not defined
#print(a)
"""
Traceback (most recent call last):
  File "/home/ubuntu/real_python/16_Exception_Handling/exception_handling.py", line 15, in <module>
    print(a)

NameError: name 'a' is not defined
"""

"""
Sometimes we have the program to do something special when exception is raised .
We can use "try/except" for such cases.
"""

# example : We have a function meant to iterate over 20 numbers from a list . However if the list  does not 
# contain 20 numbers , we can interpret '0' as the reminder of the list .

def print_num(n):
    print(n)

def catch_this():
    the_list=(1,2,3,4,5)

    for i in range(20):
        try:
            print_num(the_list[i])
        except IndexError:
            print_num(0)

catch_this()
        
