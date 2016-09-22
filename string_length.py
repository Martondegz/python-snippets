c"""
You are presented with a string or a collection of strings
Your function should return the length of the string, or strings in a list
['Fairy', 'tale'] should return [5, 4]
'C-sharp' should return [7]
"""

# form a new list
# compare the string to a str
# append the len of string to the empty list
# return list
# now compare the string to list
# append the length of string to the list
# return list 

def string_length(string):
	new_list = []

	if type(string) == str:
		new_list.append(len(string))
		return new_list

	elif type(string) == list:
		for x in string:
			new_list.append(len(string))
			return new_list

print string_length(string=raw_input())