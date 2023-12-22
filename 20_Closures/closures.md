# Closures

A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
Decorators in Python make extensive use of closures.
 
Let us get to it step by step

## Step 1 : Nested Function

aNested Function is a function within a function .
The outer function is called = enclosing function .

Important to understand that Nested Functions can access the variables within enclosing scope , in read-only mode .
However we can use "nonlocal" keyword to modify these variables.

We can further break this down to 2 steps :

 #### Step 1.1 - Variables with Nested Functions

Based on below code snippet 
we observe that there is a function defined with the function ,  called nested function (data_transmitter) .

Now the variable passed to the main function (transmit_to_space) , is accessible to the nested function .
This variable(message) is available as read-only for the nested function (we cannot modify the data)

```python
def transmit_to_space():
    "This is the enclosing Function"
    message = 10
    # Inner Function
    def data_transmitter():
        # code for the Inner Function
        print(message)
    # Call the Inner Function
    data_transmitter()

    #More code for the Outer Function
    print ("This is the Outer FUnction :" message)

print(transmit_to_space("Test Message"))
```

#### Step 1.2 - Modify variables with Nested Functions

However we can modify the variable using keyword called "nonlocal" .

Example 


```python
def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)

```
