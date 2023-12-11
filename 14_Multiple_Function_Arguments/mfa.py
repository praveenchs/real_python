"""
***  Multiple Function Arguments***

We talk about differnt ways to pass arguments to a function.

1. predefined number of args
2. variable(not defined) number of args
3. key/value pair as args

"""

#1. Predefined args , is where we clearly define the number of arguments the function would accept

def predefined(one,two,three):
    print (f"this is arg1 {one}")
    print (f'This is arg2 {two}')
    print (f'This is arg3 {three}')
    pass

predefined(1,2,3)



#2. We can also pass  variable number of args , "*args" allows a function to accept any number of positional arguments
#"args" is just a naming convention widely used and recongnized ; 
# you can replace it with any other string (example : we used "others" instead of "args")

def variable(one,two,three,*others):
    print (f"this is arg1 {one}")
    print (f'This is arg2 {two}')
    print (f'This is arg3 {three}')
    print (f'THese are other args {list(others)}')

variable(8,9,1,2,3,10,11,12)

#3. We can also pass arguments as key/value pairs , where the order of the argument does not matter .
#The **kwargs syntax allows a function to accept any number of keyword arguments (or named arguments). 
# Similar to *args, kwargs is just a naming convention. We used "key" instead of "kwargs"

def key_arguments(one,two,three,**key):
    print (f"this is arg1 {one}")
    print (f'This is arg2 {two}')
    print (f'This is arg3 {three}')
    print (f'THese are args in key-value {dict(key)}')
    print (f'This is args for key1 : {key.get("key1")}')
    print (f'This is args for key2 : {key.get("key2")}')


key_arguments(8,9,10,key1 = 'value1' , key2 = 'value2' , key3 = 'value3' )