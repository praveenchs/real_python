# Intro to Maps , Filter and Reduce

Maps,Filters and Reduce are paradigms of functional programming .
They allow programmer to write short and simple code , hiding away the complexities like loop and branching 

map and filter are in-built modules of Python . Filter though is part of functools module .


## map

#### syntax :

```python
map(function, *iterables)

```
Each element part of iterables are passed to the function .
(*) astrik means , we can pass n number of elements .


#### Additional information about map

1.  In python3 map returns a map object , which can be converted to list using built-in "list" function
example 
```python
list(map(function, *iterables))
```

2.  the number of arguments to the function , must be the number of iterables listed


#### Understand with examples

I've a list of pet names in lower case , which needs to be modified as Upercase .

Traditionally how do we solve this problem :

```python
pet_names = ['alfred', 'tabitha', 'william', 'arla']
pets = []

for cat in pet_names:
    pets.append(cat.upper())

print(pets)


```

With map function , its lot easier and flexible ...

```python
pet_names = ['alfred', 'tabitha', 'william', 'arla']

pets = list(map(str.upper,pet_names))


print(pets)


```