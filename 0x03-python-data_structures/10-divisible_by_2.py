#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    quotient = []  # empty list to be filled by function
    for q in range(len(my_list[:])):
        if my_list[q] % 2 == 0:
            quotient.append(True)
        else:
            quotient.append(False)
    return (quotient)
