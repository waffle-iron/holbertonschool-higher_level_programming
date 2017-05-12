#!/usr/bin/python3
def search_replace(my_list, search, replace):
    idx_to_replace = [i for i, x in enumerate(my_list) if x==search]
    for i in idx_to_replace:
        my_list[i] = replace
    return(my_list)
