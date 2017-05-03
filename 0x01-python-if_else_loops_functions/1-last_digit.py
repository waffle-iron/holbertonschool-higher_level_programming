#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = number % -10
elif number >= 0:
    n = number % 10
print('Last digit of {:d} is {:d}'.format(number, n)) +
if n > 5:
    print('and is greater than 5')
elif n == 0:
    print('and is 0')
elif n < 6:
    print('and is less than 6 and not 0')
    
