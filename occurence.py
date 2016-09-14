"""
input returns dictionary mapping word to it's occurence value
"olly olly in come free"
returns { olly:2, in:1, come:1, free:1 }
"""
# user input
# create a word variable with user input
# create an empty dict
# create keys as words for the empty dict and values as the word count 
# print the dict

def dictionary(sentence):

    number = 0
    lists = sentence.split(" ")
    store= {}

    for i in lists:
        number = lists.count(i)
        store[i] = number

    return store

print dictionary(raw_input())

