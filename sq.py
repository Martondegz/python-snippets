"""Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

# create raw_input for D
# create a fuction
# create variables C and H
# create the Q variable
# if Q is squared == 10000/9

# create variables for c and d
# create  an empty variable for the values
# create items variable in the for raw input 
# loop through D items and split them
# loop through the individual D items and do the math
# append the values and join them



import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)

