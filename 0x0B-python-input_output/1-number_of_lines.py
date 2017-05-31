#!/usr/bin/python3
"""
This is module 0-read_file

This module contains one function `read_file()`
"""


#!/usr/bin/python3
def number_of_lines(filename=""):
    """Write a function that returns the number of lines of a text file
    You must use the with statement
    You don't need to manage file permission/file doesn't exist exceptions.

    Args:
    filename

    Return:
    number of lines in a file
    """
    line_count = 0
    with open(filename, "r", encoding='utf-8') as my_file:
        for line in my_file:
            line_count += 1
        return(line_count)

