#!/usr/bin/python3
def remove_char_at(str, n):
    list(str)
    new_str = ''
    for i in range(len(str)):
        if i != n:
            new_str = str[i] + new_str
    return new_str
