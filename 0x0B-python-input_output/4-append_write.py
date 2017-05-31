#!/usr/bin/python3
"""
This is module 4-append_write

This module contains one function `append_write`
"""


def append_write(filename="", text=""):
    """
    Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
    If the file doesn't exist, it should be created
    You must use the with statement
    You don't need to manage file permission/file doesn't exist exceptions.
    You are not allowed to import any module

    Args:
    filename
    text

    Return:
    number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
    with open(filename, 'r', encoding='utf-8') as my_file:
        return(my_file.read(text))
