"""Objects are encapsulation of variables and functions into a single entity .
Objects get their variables and functions from classes.
Classes are essentially template to create your object"""

"""Alternate way to understand class and object is , think of your self an architect . You create a blueprint for a 3 BHK house
, with all details like - How many Doors,Windows,location of kitchen .
Now every time a customer ask you to build a house , you will use this blue print to build the actual house with wooden door,
Glass windows and island kitchen .
Here Class is Blueprint and House is the Object"""


# Simple Class
class MyClass:
    variable = 'blah'

    def Function(self):
        print("This is a message inside class")

# Assign above object to class
myobject = MyClass()
myobject1 = MyClass()

# Accessing Object variables 
# print the variable define in myclass
print(myobject.variable)

# Same way to access the Object Functions , with following example . Since its a function makesure to apend "()" to
# the functions name 

print(myobject1.Function())


# Use of init function in Class

# "The __init__()" function , is a special function called when the class is being initiated .
# Its used to assign values in the class .

class NumberHolder:

    def __init__(self,number):
        self.number = number
    
    def returnnumber(self):
        return self.number
# Assign class "NumberHolder" to the Object "var"
var = NumberHolder(7)

print(var.returnnumber())


