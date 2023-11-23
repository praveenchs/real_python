# python uses boolean logic to evaluate conditions . True/False are returned when expression is compared or evaluated .
# Usecase is if condition is met , execute this code otherwise exit the program ..

# example 

x = 2

print ( x == 2)
print ( x > 3)

# Notice that variable is defined using single equal to ("="), where as the condition is evaluated using "=="
#  Not equal to operator is marked as "!="
#If you run above code this should print true/false based on the condition .



# Boolean Operators

# The "and" / "or" boolean operators allow building complex expressions , for example 


name = "Praveen"
age = 43

if name == "Praveen" and age == 43:
    print (f"His name is {name} , of age {age}")

if name != "Praveen" or age == 43:
    print (f"Dont think he is {name} as he is doesnt look {age}!")




# ** In Operator **

# In operator helps to check if the  object is within the list or tuple 

name = "Praveen"
name_list = ["Pavi","Ravi","breeze","Praveen"]

if name in name_list:
    print(f"{name} belongs to this Team")


# Code Blocks and "if" statements
# we create a block of code using indentation . Indentation can be created using tab or 4 spaces .
# Example of how to create indentation 
# Is operator does not match the value of the variable but the instances themselves


name = "Praveen"
age = 43

if name is "Praveen":
    print (f" name is {name}")
    pass
elif age is 43:
    print (f"Praveen doesnt look {43}")
    pass
else:
    print (f"Dont know who he is")
    pass


# "not" operator
#use of "not" operator before a boolean expression inverts it 

print(not False)
print(not False == True)



# Excercise on Conditions

# Change variable so that each if statement becomes true 

number = 16
second_number = 0 # In python zero is considered falsy value
first_array=[1]
second_array=[1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 3:
    print("4")

if len(first_array) and first_array[0] == 1:
    print("5")

if not second_number: # This line checks if "second_number" evaluates to 'False' . As python considers zero as falsy value , then the condition is met 
    print("6")