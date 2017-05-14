#!/usr/bin/python3
"""
This module "4-print_square" is task 3
for 0x06-python-test_driven_development and
completed for Holberton School coursework.

This module supplies one function: print_square().

To test, run: `python3 -m doctest -v ./tests/4-print_square.txt`
"""


def print_square(size):
    """
    This function prints a square with the character #.

    Arguments:
    size is the size length of the square and must be an integer
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    else:
        print('\n'.join(['#' * size for j in range(size)]))
