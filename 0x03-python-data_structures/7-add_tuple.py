#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # store tuple length into new variables
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)

    # if tuple is bigger than 2, use only first 2 ints
    if len_tuple_a > 2:
        len_tuple_a = 2
    if len_tuple_b > 2:
        len_tuple_b = 2

    # create list, also accounts for missing integer
    list_a = [0, 0]
    list_b = [0, 0]

    # loop through tuple lengths, insert ints into list
    for i in range(len_tuple_a):
        list_a[i] += tuple_a[i]
    for i in range(len_tuple_b):
        list_b[i] += tuple_b[i]

    tuple_sum = (list_a[0] + list_b[0],
                 list_a[1] + list_b[1])
    return (tuple_sum)
