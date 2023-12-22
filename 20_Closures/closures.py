def transmit_to_space(message):
    # "This is the enclosing Function"
    message = 10
    # Inner Function
    def data_transmitter():
        # code for the Inner Function
        print(message)
    # Call the Inner Function
    data_transmitter()

    #More code for the Outer Function
    print ("This is the Outer Function :" , message)


# Call the enclosed function
print(transmit_to_space("Test Message"))



""" # use keyword nonlocal
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number # this overwrites the value from enclosing function
        number=8
        print(number) # number =3 as defined in the previous line
    printer()
    print(number)# number=3 ,as we use the keyword nonlocal 

print_msg(4) """