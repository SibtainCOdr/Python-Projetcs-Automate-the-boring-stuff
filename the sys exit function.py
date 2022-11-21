import sys
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You have typed' + response )



    #if you add the '+' after the response variable in 7th line it causes and error, so if you want
    #  to add something afer the variable only then use the second + 