#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)  # check if idx is out of range
    if idx < len(my_list):
        return (list(idx))
    return(None)
