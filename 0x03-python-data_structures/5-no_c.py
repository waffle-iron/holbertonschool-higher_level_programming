#!/usr/bin/python3
def no_c(my_string):
    no_more_c = ""  # declare empty variable to be filled with output
    for char in my_string:  # traverses through each character in string
        if char != 'c' and char != 'C':  # exclude upper/lower case C
            no_more_c += char  # store remaining characters into variable
    return(no_more_c)
