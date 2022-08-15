'''14.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''
lowercase = []
uppercase = []
box = input("Enter Something : ")
for items in box:
    if items.islower():
        lowercase.append(items)
    if items.isupper():
        uppercase.append(items)
print('Upper Case Letter in THe Given String Is',len(uppercase))
print('Lower Case Letter in THe Given String Is',len(lowercase))