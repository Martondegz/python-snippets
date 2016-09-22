"""Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each 
digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input"""

# create a list 
# append the even numbers between 1000 and 3000 to the list
# print out the numbers
# call the function

x=[]
even = [num for num in range(999, 3001) if num % 2 == 0]
x.append(even)
print str(x).strip('[]')


