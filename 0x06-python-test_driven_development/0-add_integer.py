#!/usr/bin/python3
"""
This module "0-add_integer" is task 0
for 0x06-python-test_driven_development and
completed for Holberton School coursework.

This module supplies one function: add_integer().

To test, run: `python3 -m doctest -v ./tests/0-add_integer.txt`
"""


def add_integer(a, b):
    """
    This function calculates the sum of two integers

    Arguments:
    a: integer, if type float, will be cast to integer
    b: integer, if type float, will be cast to integer

    Return:
    a + b or raise error if input is not an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    cast_a = int(a)
    cast_b = int(b)
    return (cast_a + cast_b)
