from functools import reduce

numbers = [1,2,3,4,5]

def product(x,y):
    return x*y

sum = reduce(product,numbers)
print (sum)

# redo with lambda

lambda_product = reduce((lambda x,y : x * y),numbers)

print(lambda_product)