#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    idx_to_replace = [i for i, x in enumerate(new_list) if x == search]
    for i in idx_to_replace:
        new_list[i] = replace
    return(new_list)
