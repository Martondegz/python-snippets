while True:
    name = raw_input('enter name:')
    if name == 'stop':break #breaks the statement so that the age input follows
    age = raw_input('enter age:')
    print ('Hello', name, '=>', int(age) ** 2)
