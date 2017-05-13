#!/usr/bin/python3
def add_integer(a, b):
    """Returns a + b.

    Works with integers:

    >>> add_integer(2, 3)
    5
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    int(a, b)
    return a + b
