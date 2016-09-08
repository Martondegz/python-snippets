# create a variable i 
# create a list variable
# create a while loop for numbers less than 10
# print out the i number
# append it to the numbers list
# loop through the the next number
# print that number out
# 
# break
i = 0 	
numbers = []

while i < 10:
	print "this the number at the top %d" %i
 	numbers.append(i)

 	i = i + 1
 	print "Number now:", numbers
 	print "this is the number at the bottom %d" %i 
print "The numbers"	
for num in numbers:
	print num
