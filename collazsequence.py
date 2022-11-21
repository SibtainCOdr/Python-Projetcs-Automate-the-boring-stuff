
from unittest import result


def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return(result)
    else:
        result = 3 * number + 1
        print(result)
        return(result)

print("Enter your number: ")
number = int(input())

while number != 1:
    number = collatz(number)