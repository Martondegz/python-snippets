"""return binary out of remainder of an integer when divided by two"""
from pythonds.basic.stack import  Stack

def divide_by_2(num):
    rem_stack = Stack() # putting my stack in action

    while num > 0:
        rem = num % 2 # remainder variable
        rem_stack.push(rem) # push the remainder in my stack
        num = num // 2 # divide my num by two

    bin_string = '' # create my binary string
    while not rem_stack.isEmpty():
        bin_string = bin_string + str(rem_stack.pop()) # pop the remainder from my stack
    return bin_string # get my binary string

print divide_by_2(457)
