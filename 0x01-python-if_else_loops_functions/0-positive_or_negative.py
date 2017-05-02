#!/usr/bin/python3
import random
number = random.randint(-10, 10)
n = 
if n < 0:
    print('{:d} {}'.format(n, 'is negative'))
elif n == 0:
    print('{:d} {}'.format(n, 'is zero'))
else:
    print('{:d} {}'.format(n, 'is positive'))
