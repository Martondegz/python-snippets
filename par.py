# Write a function that return whether or not the input string has balanced parentheses
# Balanced:
#   '((()))'
#   '(()())'
# Not balanced:
#   '((()'
#   '())('

# use input for a string

from pythonds.basic.stack import Stack


def parChecker(symbolString):
    s = Stack() # stack method applied
    balanced = True # bool value true if par is balanced
    index = 0
    while index < len(symbolString) and balanced: # loops through the symbolString
        symbol = symbolString[index] # assign a symbol var to the symbolString index
        if symbol == "(":    # condition set
            s.push(symbol) # push the  symbol on the stack
        else:
            if s.isEmpty(): # when stack is empty
                balanced = False # no balance
            else:
                s.pop() #  else remove the the symbol from the stack


        index = index + 1 # start up  indexing of the symbolString


    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(('))

