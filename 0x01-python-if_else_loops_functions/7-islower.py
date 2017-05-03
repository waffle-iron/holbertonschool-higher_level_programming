#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z')):
        if c == i:
            return True
    return False
