"""
*** Sets ***

Sets are like lists , but 

    1. Does not have duplicates
    2. unordered list , there is no index to retrieve the element .

Usecases:

You can compare 2 sets to get intersection and deviations between sets.
Example :

You have 2 sets of data , of the employees who attended 2 different events : A and B

you can indentify who attended both using "intersection" method

$$$ Sets are best understood using venn diagram

"""

# Create set from a sentence, 

print(set("Jack and Jill went up the Hill , Jack fell down".split()))

# output : 	{'Jack', 'Hill', 'fell', 'down', 'up', 'Jill', 'went', 'and', 'the', ','}
# Above output has Jack once as the set inheriently removes duplicate elements .


# Example for Intersection

a = {'Jack','Jim','Jill'}
b = {'Bob','Shyam','Jill'}

print(a.intersection(b))
print(b.intersection(a))

# To know which member attended one of the events use "symmetric_difference"
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# Use difference method to get elements in A , which do not match elements in B
print(a.difference(b))
#{'Jack', 'Jim'}
print(b.difference(a))
#{'Jack', 'Jim'}

# What is the difference between "symmetric difference" and "difference"
# "symmetric difference" contains elements unique to both sets
# "difference" contains elements unique to the set where the method is used .


# Union Method , contains all elements from both sets
print(a.union(b))
#{'Shyam', 'Jill', 'Bob', 'Jim', 'Jack'}


