birthdays = {'sibain': '9 March', 'shahnain':'26 july', 'zeeshan':'11 February', 'annan': '27 May'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birth day of '+ name )
    else:
        print('I do not know have birthday information for ' + name)
        print('What is their birhday? ')
        bday = input()
        birthdays[name] = bday
        print('Birthday database has been updated')
