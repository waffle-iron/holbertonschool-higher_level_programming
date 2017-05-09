#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listcopy = my_list[:]
    if listcopy is None:
        return
    if idx < 0 or idx > len(listcopy) - 1:
        return(listcopy)
    listcopy[idx] = element
    return(listcopy)
