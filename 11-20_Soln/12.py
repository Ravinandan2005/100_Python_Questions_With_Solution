'''12.Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.The numbers obtained should be printed in a 
comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

'''
even_num = []
for num in range(1000,3001):
    if num%2==0:
        even_num.append(str(num))#String only can be joined using csv
print(",".join(even_num))