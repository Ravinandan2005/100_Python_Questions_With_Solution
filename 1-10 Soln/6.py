'''6. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
For example Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24'''

from math import sqrt
num = input('Enter any num : ')
lst = num.split(",")
newlst = []
c,h = 50,30
for values in lst:
    q = round(sqrt(2*c*int(values)/h))
    newlst.append(q)
print(newlst)