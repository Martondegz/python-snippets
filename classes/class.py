"""Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters"""
class InputOutPrint():
    def __init__(self): # use the method to help in create parameters and instantiation of methods
        self.s = ''
    def getString(self):
        self.s = raw_input() # input to be put
    def printString(self):
        print self.s.upper() # output in uppercase

strObj = InputOutPrint()
strObj.getString()
strObj.printString()
