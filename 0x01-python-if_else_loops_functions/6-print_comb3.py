#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != j:
            print('{}'.format(i), end='')
            if i == 8:
                print('{}'.format(j))
            else:
                print('{:d}, '.format(j), end='')
