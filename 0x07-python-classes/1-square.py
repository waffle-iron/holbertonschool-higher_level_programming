#!/usr/bin/python3
"""
This module "1-square" is task 1 for 0x07-python-classes
and completed for Holberton School coursework.

This module contains one class: Square
"""


class Square:
    """
    This class defines a square based on 0-square

    **Task parameters:**
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module

    **Functions**
    __init__(self, size)

    **Example**
    my_square = Square(3)
    """

    def __init__(self, size):
        """
        instantiate an object based on Square class

        Arguments:
        size - no type/value verification
        """
        self.__size = size
