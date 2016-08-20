# Completed extended par_checker for: [,{,(,),},]
from pythonds.basic.stack import Stack

def par_matcher(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string):
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1
    if balanced  and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    open = "([{"
    close = ")]}"
    return open.index(open) == close.index(close)

print (par_matcher("(((([[]]]]))}}"))
print (par_matcher("(((([[]]))))"))

