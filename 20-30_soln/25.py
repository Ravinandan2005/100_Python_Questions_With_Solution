'''Define a class, which have a class parameter and have a same instance parameter.

Hints:
Define an instance parameter, need add it in __init__ method.You can init an object
 with construct parameter or set the value later'''

class Calculator():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        print(self.num1+self.num2)
add = Calculator(5,4)
add.sum()
