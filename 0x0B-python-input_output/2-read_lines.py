#!/usr/bin/python3
"""
This is module 2-read_lines

This module contains one function `read_lines`
"""


def read_lines(filename="", nb_lines=0):
    """
    Write a function that reads n lines of a text file (UTF8) and prints it to stdout:
    Read the entire file if
    nb_lines is lower or equal to 0 OR
    greater or equal to the total number of lines of the file
    You must use the with statement
    You don't need to manage file permission/file doesn't exist exceptions.

    Args:
    filename
    nb_lines

    Return:
    prints specific lines to stdout
    """
    line_count = 0
    with open(filename, "r", encoding='utf-8') as my_file:
        if nb_lines <= 0:
            print(my_file.read(), end="")
        else:
            for line in my_file:
                if line_count < nb_lines:
                    print(line, end="")
                    line_count += 1
