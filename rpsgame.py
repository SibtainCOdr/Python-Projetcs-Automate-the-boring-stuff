import random, sys

print('Rock, Paper, Scissors')



wins = 0
losses = 0
ties = 0

while True:
    print(f'wins, {wins}, losses, {losses}, ties, {ties}') 
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit ')
        playermove = input()
        if playermove == 'q':
            sys.exit()
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break
        print('Type one of r, p, s, or q')

    if playermove == 'r':
        print('Rock versus...')
    elif playermove == 'p':
        print('Paper versus...')
    elif playermove == 's':
        print('Scissors versus...')

    randomnumber = random.randint(1, 3),
    if randomnumber == 1:
        computermove = 'r'
        print('Rock')
    elif randomnumber == 2:
        computermove = 'p'
        print('Paper')
    elif randomnumber == 3:
        computermove = 's'
        print('Scissors')

    if playermove == computermove:
        print('Its a tie! ') 
        ties = ties + 1
    elif playermove == 'r' and computermove == 's':
        print('You win!')
        wins = wins + 1
    elif playermove == 'p' and computermove == 'r':
        print('You win! ')
        wins = wins + 1
    elif playermove == 's' and computermove == 'p':
        print('You win!')
        wins = wins + 1
    elif playermove == 'r' and computermove == 'p':
        print('You lose!')
        losses = losses + 1 
    elif playermove == 'p' and computermove == 's':
        print('You lose!')
        losses = losses  + 1
    elif playermove == 's' and computermove == 'r':
        print('You lose!')
        losses = losses + 1
