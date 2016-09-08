"""Write a program that accepts sequence of lines as input and 
prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT"""

# create a list variable
# create a while loop  to loop over my list
# create a raw input variable for my input
# set an if condition for my statement
# append my statements to the list when they are in uppercase
# for any sentence in my list print out the sentence

lines = []

while True:
	s = raw_input()
	if s:
		lines.append(s.upper())
	else:
		break; 
for sentence in lines:
	print sentence
 
	


