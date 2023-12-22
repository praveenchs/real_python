pet_names = ['alfred', 'tabitha', 'william', 'arla']
pets = []

for cat in pet_names:
    pets.append(cat.upper())

print(pets)

# achieving this with maps

pet_names = ['alfred', 'tabitha', 'william', 'arla']

pets = list(map(str.upper,pet_names)) 

print(pets)


# pass multiple arguments to maps

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

round_off = list(map(round,circle_areas,range(1,7)))
print(round_off)
    
# what if we pass fewer elements with one of the arguments , maps terminate after most sucessful iterables (where both iterables have a value).
round_off_few = list(map(round,circle_areas,range(1,4)))
print(round_off_few)



""" 
excercise 

To consolidate our knowledge of the map() function, we are going to use it to implement our own custom zip() function. 
The zip() function is a function that takes a number of iterables and then creates a tuple containing each of the elements in the iterables.
Like map(), in Python 3, it returns a generator object, which can be easily converted to a list by calling the built-in list function on it. 
Use the below interpreter session to get a grip of zip() before we create ours with map()

"""

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

result = list(zip(my_strings,my_numbers))

print(result)

# what if the iterables are not of the same length

my_strings = [ 'b', 'c', 'e']
my_numbers = [1, 2, 3, 4, 5]
result = list(zip(my_strings,my_numbers))

print(result)