#!/usr/bin/python3
import random
number = random.randint(-100, 100)
if number > 5:
    print('{} {:d} {} {: d} {}'.format('Last digit of', number, 'is', number % 10, 'and is greater than 5'))
elif number == 0:
    print('{} {:d} {} {: d} {}'.format('Last digit of', number, 'is', number % 10, 'and is 0'))
elif number < 6:
    print('{} {:d} {} {: d} {}'.format('Last digit of', number, 'is', number % 10, 'and is less than 6 and not 0'))
