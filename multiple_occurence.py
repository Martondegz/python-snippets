"""
You are presented with two arrays, all containing positive integers.
One of the arrays will have one extra number, see below:
[1,2,3] and [1,2,3,4] should return 4
[4,66,7] and [66,77,7,4] should return 77
"""
# pseudocode 
# def a function with list as arguments
 

def list_array(a, b):
 # a=[1,2,3] b=[1,2,3,4]

	holder = 0 # a variable to hold the different element in the both list

 	if len(a) > len(b):
 		
 		list1 = (set(a) - set(b)) # this is the point where list can use operators
 		
 		holder = list1.pop() # removes  the element from the list
 		
 		return holder
 	
 	elif len(b) > len(a):
 		

 		list2 = (set(b) - set(a))
 		
 		holder  = list2.pop()

 		return holder
 	else:
 		return 0


 

print list_array()	








