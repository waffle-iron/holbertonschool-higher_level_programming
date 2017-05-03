#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
        if i % 2 != 0:
                i = i - ord(' ')
        print('{}'.format(chr(i)), end='')
