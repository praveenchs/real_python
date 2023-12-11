# use of loc and iloc to retrieve selective data

# loc is label-based , means you have to specify rows and columns based on their row and columns labels.
# In this example , print observations for Australia and Egypt
import pandas as pd

# Use the country column as index (column 1) 

cars = pd.read_csv('cars.csv',index_col=1)

# Use loc method and filter table for Australia and Egpyt . We should see data only for these 2 contries

print(cars.loc[['Australia','Egypt']])

## Use loc to filter table for countries which drive on right side
cars_drive = pd.read_csv('cars.csv',index_col=0)
print(cars_drive.loc[cars_drive['drives_right']==True])



## iloc is integer index based , so we filter by their integer index just like "Indexing" or list slicing .

# Print the last 2 rows
print(cars[-2:])

#pringt first 2 rows 
print(cars[0:2])
