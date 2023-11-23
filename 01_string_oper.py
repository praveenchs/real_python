string = "Hello Wor-ld!"
print(string.split("-"))

mys = "Hi Praveen,Good to see you work hard"

print("Length of mystring %s" % len(mys))

# Index of first occurance of an alphabet 

print (mys.index("e"))

# number of occurance of the alphabet

print ( "The number of times letter 'o' occurs : %s" %mys.count("o"))

# Slicing

print ("The first five characters are %s" % mys[:6])
print ("The next five characters are %s" % mys[5:10])
print ("The even charecters are %s " %mys[::2])
print ("The 13th char %s" %mys[12])
print ("The characters with odd index are %s" %mys[::2])
 
#'[-5:]' is slice notation .start:stop . start -5 we meant start from fifth character from the last (counting from the last character) , empty after ':' means till last character
print ("The last 5 characters are: %s" %mys[-5:]) 

print("Covert every character to Uppercase : %s" %mys.upper())
print("Convert every character to lowercase: %s" %mys.lower())
if mys.startswith("Hi"):
    print("String starts with 'Hi'")

if mys.endswith("hard"):
    print("String ends with 'hard'")

print ("split the sentence into list of words : %s" % mys.split())
