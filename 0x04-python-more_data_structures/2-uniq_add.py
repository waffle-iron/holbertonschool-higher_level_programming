#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:  # check if list exists
        return None
    unique = set(my_list)
    return(sum(unique))
