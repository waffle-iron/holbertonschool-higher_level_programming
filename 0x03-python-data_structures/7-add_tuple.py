#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)

    if len_tuple_a > 2:
        len_tuple_a = 2
    if len_tuple_b > 2:
        len_tuple_b = 2

    list_a = [0, 0]
    list_b = [0, 0]

    new_tuple = (list_a[0] + list_b[0],
                 list_a[1] + list_b[1])
    return (new_tuple)
