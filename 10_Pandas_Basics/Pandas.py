"""Pandas are high level data manupluation tool , built on top of numpy.
Its key data structure is called DataFrame.
DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables"""

# One way to create a DataFrame is to use a dictionary 

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

# Import pandas package as pd
import pandas as pd

# Convert dictionary to DataFrames

brics = pd.DataFrame(dict)
print(brics)

# As you can see the dataframe, Pandas has assigned an index for each row (0-4) 
#If you like to use a different index value say the two letter country code you can do that as well .

#set index for brics
brics.index = ["BR", "RU" , "IN" , "CH" , "SA"]
print(brics)



#Another way to create dataframe is to use csv file with pandas .

import pandas as pd

cars = pd.read_csv('cars.csv')

print(cars)



