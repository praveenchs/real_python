""" 

**Numpy Array**

Numpy Arrays are alternative to Python Lists .

Advantages of Numpy over lists :

    1.  Fast
    2.  Easy to work 
    3.  allows calculation across arrays


"""

"""Example : Creat Numpy Arrays
"""

# Create lists 
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# import numpy as np
import numpy as np

# Create numpy array from above list
np_height = np.array(height)
np_weight = np.array(weight)


# Print the numpy array type
print(type(np_height))

"""Element-wise calculations"""

# Calculate BMI based on the data (Height,Weight)
bmi = np_weight / np_height ** 2
print(bmi)

# Subsetting
# Subset is where we can create a subset of array based on condition

# Example , create a subset of elements where the bmi is above 25 .
print(bmi[bmi > 25])



