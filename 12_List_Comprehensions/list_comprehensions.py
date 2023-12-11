""" 
*** List Comprehensions ***

List Comprehensions is a powerful tool , which creates a new list based on another list .

"""


# Example : create a list of integers based on the number of words in the given sentence , except for the word "the"

sentence = "the quick brown fox jumps over the lazy dog"

sentence_split = sentence.split()
#print(sentence_split)
sentence_int = []

for word in sentence_split:
    if word == 'the':
        continue
    else:
        sentence_int.append(len(word))

print(sentence_int)


# Using a list comprehension , we can simplify the process
words = sentence.split()
word_length = [len(word) for word in words if word != "the"]
print(word_length)