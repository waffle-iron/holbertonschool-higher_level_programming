#!/usr/bin/python3
"""
This module is task 3 for 0x06-python-test_driven_development

This module supplies one function: `print_square`

To test, a text file is provided in the /tests directory. To run:
`python3 -m doctest -v ./tests/4-print_square.txt`
"""
def print_square(size):
    """
    This function prints a square with the character #.

    Arguments:
    size is the size length of the square and must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:

