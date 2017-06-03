#!/usr/bin/python3
"""
This is module 3-write_file

This module contains one function `write_file`
"""


def write_file(filename="", text=""):
    """
    Write a function that writes a string to a text
    file (UTF8) and returns the number of characters written:
    You must use the with statement
    You don't need to manage file permission exceptions.

    Args:
    filename
    text

    Return:
    number of characters written
    """
    with open(filename, "r+", encoding="utf-8") as my_file:
        char_count = my_file.write(text)
    return (char_count)
