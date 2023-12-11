"""
Exercise

Write a program using lambda functions to check if a number in the given list is odd. 
Print "True" if the number is odd or "False" if not for each element.

"""
l = [2,4,7,3,14,19]

def odd(int_list):
    for number in int_list:
        if number % 2 != 0:
            print("True")
        else:
            print("False")


#print(odd(l))

# Write this in Lamda

#odd_lambda = lambda int_labda_list : for i in 

for i in l:
    # your code here
    my_lambda = lambda x : (x % 2) == 1
    print(my_lambda(i))