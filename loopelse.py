#determines whether a positive integer y is prime by searching for factors greater than 1
# foor instance y = 10



x = 2  #for some y > 1
while x > 1:
    if 2 % x == 0: #remainder
        print (2,'has factor', x)
        break #skip else
    x -= 1
else:
    print(10,'is prime')  #normal exit