# "for" loop , itreates over a given list of elements in sequence 

# for loop can be used for list or tuples 
# example print each element in the list below

even = [2,4,6,8,10]

for element in even:
    print(element)

# sequence of numbers can be defined using "range" or "xrange" . Python uses range function , which acts like xrange

for element in range(2,11,2):
    print(element)


# "While" loop repeats as long as the condition is not met

count = 0
while count < 5:
    print(count)
    count += 1

# Break is used to exit a loop (for/while)

count = 0 
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Continue is to skip current block .

for x in range(10):
    # check if x is even
    if x % 2 == 0:
        continue
    print(x)

#  "Else" statement 

count = 0
while(count<5):
    print(count)
    count += 1
else:
    print("count value reached %d" %(count))

# "Else" with "break" 

for i in range(1,10):
    if(i%5==0):
         break
    print(i)
else:
    print("not print due to break but not due fail in condition")

# excercise for loops

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# print out all even numbers from the list in the same Order
## logic : print all even number using "%" operator
# Dont print any number that comes after 237 in the sequence 
## logic: break when the number is 237 
## first look for number 237 and perform break , inside this condition print even number

for number in numbers:
    if number == 237:
        break
    if number % 2 == 1:
        continue
    print(number)
    

    

         