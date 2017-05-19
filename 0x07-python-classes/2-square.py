#!/usr/bin/python3
"""
This module "2-square" is task 2 for 0x07-python-classes
and completed for Holberton School coursework.

This module contains one class: Square
"""


class Square:
    """
    This class defines a square based on 1-square

    **Task parameters:**
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    You are not allowed to import any module

    **Functions**
    __init__(self, size)

    **Example**
    my_square_1 = Square(3)
    """

    def __init__(self, size=0):
        """
        instantiate an object based on Square class

        Arguments:
        size must be an integer
        size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
