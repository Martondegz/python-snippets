while True:
    name = raw_input('enter name:')
    if name == 'stop':break
    age = raw_input('enter age:')
    print ('Hello', name, '=>', int(age) ** 2)
