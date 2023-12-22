# Filter

As the name suggest , unlike map which passes **every** elements to a function . Filter tend to run the elements through a condition before passing the elements to the function .

## syntax 

filter(func,iterable)

## note for filter

1.  Filter takes only **one iterable** , unlike map which accepts multiple iterable (*iterable)
2.  the func argument is required to return a **boolean type** , for the filter to process the element . If the value from the function is not boolean , it simply returns the iterable passed to it.
3.  Filter passes each element in the iterable through func and returns **only** the one which evaluate to true.


Example :
The following is a list (iterable) of the scores of 10 students in a Chemistry exam. Let's filter out those who passed with scores more than 75...using filter.


```python
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(scores):
    if score > 75:
        return true
    else false:



```