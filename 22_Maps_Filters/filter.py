scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65,83]


def is_A_student(score):
    return score > 75 # this logic should always return a boolean

over_75 = list(filter(is_A_student,scores))

print(over_75)


# lets filter palindromes from the below tuple
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

def palindromes(word):
    return word == word[::-1]

filter_pali = list(filter(palindromes,dromes))
print(filter_pali)

# re-write it using lambda
filter_lambda = list(filter(lambda words : words == words[::-1],dromes))
print(filter_lambda)




     
