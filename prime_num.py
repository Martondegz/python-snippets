# Write a function that accepts a number and return a boolean based on
# whether it's a prime number.

# create a function
def is_Prime(num):

# use an if statement to give the prime input condition
    if num % 2 == 0:  # even numbers
        return False
    elif num < 2: # prime numbers start from 2
        print False
    for factor in range(3, int(num ** 0.5)+1, 2):
        if num % factor == 0:
            return False
        return True
print is_Prime(num = int(raw_input("gimme a number!! ")))
