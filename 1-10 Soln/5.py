'''5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
Hints:
Use init method to construct some parameters
'''
string= input('Enter any string : ')
class TM():
    def __init__(self,string):
        self.string = string
    def getString(self):    
        print(f'{self.string}')
    def printString(self):    
        print(f'{self.string.upper()}')
        
q=TM(string)
q.getString()
q.printString()