"""
Exercise

Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more) 
The foo function must return the amount of extra arguments received. 
The bar must return True if the argument with the keyword magicnumber is worth 7, and False otherwise.

"""

def foo(a, b, c,*d):
    return len(list(d))

def bar(**args):
    if args.get("magicnumber") == 7:
        return True
    else:
        return False
    

#print(foo(1,2,3,4,5,6,7,8,10))
#print(bar(notmagic = 1 , magicnumber = 0 , a = 'aplha' ,b = 'beta'))

# test code
if foo(1,2,3,4,5) == 2:
    print ("ok")
if foo(1,2,3,4,5,6,7,8) == 5:
    print ("good")
if bar(magic='number',magicnumber=7) == True:
    print ("Great")
if bar(magic='number',magicnumber=77) == False:
    print ("Awesome")