# Given a number whose digits are unique, find the next larger number that can be formed with those digits.
# For example: 241 will output 421, 27 will output 72 and 68734 will output 87643
def larger_num(num):
# convert to string
    num_str = str(num)
# create a empty list
# add each the char to list
    lst = [x for x in num_str]
# sort list in ascending order
    n_list = sorted(lst, reverse=True)
# join list and convert to int
    return int("".join(n_list))
print larger_num(2365)