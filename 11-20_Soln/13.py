'''13.Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
alpahabets = []
numbers = []
box = input('Enter Something : ')
for items in box:
    if items.isalpha():
        alpahabets.append(items)
    if items.isdigit():
        numbers.append(items)
print('Total Letters : ',len(alpahabets))
print('Total Numbers : ',len(numbers))        