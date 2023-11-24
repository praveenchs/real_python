"""In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

Run and see all the functions work together!"""

 

 # function list_benefits
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# function build_sentence(info)

def build_Sentence(info):
    return info + " is a benefit of functions!"

#list_benefits_var = list_benefits()

#for info in list_benefits_var:
#    x = build_Sentence(info)
#    print(x)

def benefits_of_function():
    list_benefits_var = list_benefits()
    for info in list_benefits_var:
        print(build_Sentence(info))

benefits_of_function()
