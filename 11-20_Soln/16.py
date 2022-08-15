'''16.Use a list comprehension to square each odd number in a list. The list is input by a 
sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

1,2,3,4,5,6,7,8,9
Then, the output should be:

1,9,25,49,81
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
#Note The Condition is using list comprehension
a = 1,2,3,4,5,6,7,8,9
oddsq_num = []
lst = list(a)
for num in a :
    if num%2!=0:
        oddsq_num.append(str(num**2))
print(",".join(oddsq_num))
