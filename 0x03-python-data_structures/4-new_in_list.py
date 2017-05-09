# Write a function that replaces an element in a list at specific position without modifying the original list.
# Prototype: def new_in_list(my_list, idx, element):
# If idx is out of range, the function should
# return a copy of the original list
# You are not allowed to import any module
# You are not allowed to use try/except

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    listcopy = my_list
    listcopy[idx] = element
    return(listcopy)

    
