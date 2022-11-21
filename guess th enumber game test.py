#this is a number guessing game
import random

print('I am think of a number between 1 to 20')
secretnumber = random.randint(1, 20)

for guesstaken in range(1, 7):
    print('take a guess')
    guess = int(input())
    if guess < secretnumber:
        print('Your guess is too low')
    elif guess > secretnumber:
        print('Your guess is too high')
    else:
        break

if guess == secretnumber:

    print('Well done, you guessed my number in ' + str(guesstaken) +' tries')
else:
    print('You were unable to guess the number, the number was' + str(secretnumber))
