#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    listcopy = my_list[:]
    listcopy[idx] = element
    return(listcopy)
