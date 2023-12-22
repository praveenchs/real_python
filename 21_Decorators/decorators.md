# Decorators

Decorators allows you make simple modifications to callable objects : functions , classes or methods 

We will use decorators with functions with examples

```python
@decorator
def function(arg):
    return value

# Is equivalent to:
def function(arg):
    return value

# this passes the function to the decorator and reassigns it to the functions
function = decorator(function) 

```