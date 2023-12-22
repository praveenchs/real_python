"""
Code introspection is the ability to examine classes, functions and keywords to 

1.  know what they are, 
2.  what they do and 
3.  what they know


Python provides several functions and utilities for code introspection.

help()
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance()  
__doc__ 
__name__
"""

#Often the most important one is the "help" function, since you can use it to find what other functions do.

"""
Exercise
Print a list of all attributes of the given Vehicle object.

"""
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
print(dir(Vehicle))