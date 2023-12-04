#Excercise
"""First, convert the list of weights from a list to a Numpy array. Then, convert all of the weights from kilograms to pounds.
 Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds."""



import numpy as np

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


np_weight_kg = np.array(weight_kg)
np_weight_pound = np_weight_kg * 2.2


print(np_weight_pound)

