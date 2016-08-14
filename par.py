# Write a function that return whether or not the input string has balanced parantheses
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
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()


        index = index + 1


    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(('))

