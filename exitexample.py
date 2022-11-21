#This is an example of the sys.exit() function
import sys

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print(' You typed ' + response +'.')