""" Dictionaries is a data type  , which is a combination of key,value pair.
 Each value stored can be accesed using its key . Just like how index is used with list . """

# create a phone number database , with name and phone number

#step 1.1 : create an empty dictonary using curly brackets
phonebook = {}

#step 2 : add name,number to the dictionary

phonebook["John"] = 83723467
phonebook["Doe"] = 83734984
phonebook["Peter"] = 92583987

# Step 3 : Read the dictionary
print(phonebook)

# Step 1.2 : Alternate method to create dictionary

phonebook1 = {
    "John" : 83723467,
    "Doe" : 83734984,
    "Peter": 92583987
}

print(phonebook1)



""" Iterating over dictionaries :
 We can Iterate over  dictionaries like list , however dictionaries does not keep maintain ordered list 

 """

for name,number in phonebook.items():
    print("Phone number if %s is %d" %(name,number))

# Delete a kvp in dictionary

del phonebook1["John"]
print(phonebook1)

# Alternate way to delete is use of "pop"

phonebook1.pop("Peter")
print(phonebook1)