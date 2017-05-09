#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):  # check if index is in range
        return (my_list)
    if my_list is None:  # check if my_list exists
        return (None)
    del my_list[idx]
    return(my_list)

