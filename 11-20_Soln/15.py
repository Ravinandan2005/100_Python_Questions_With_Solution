# 15.Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
num = input("Enter value: ") #getting as a string so that it can replicate

a = num * 1
aa = num * 2
aaa = num * 3
aaaa = num * 4
#converting to integers to find the sum
total = int(a) + int(aa) + int(aaa) + int(aaaa)
print(total)