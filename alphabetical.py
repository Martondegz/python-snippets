"""Write a program that accepts a comma separated sequence of words as input and 
prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input."""

# take a user input
# breakdown the words to form a list
# sort the list
# display the sorted words
#
my_str = raw_input()
words = my_str.split()
words.sort()
print ",".join(str(word) for word in words)














