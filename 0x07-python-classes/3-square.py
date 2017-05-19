#!/usr/bin/python3
"""
This module "3-square" is task 3 for 0x07-python-classes
and completed for Holberton School coursework.

This module contains one class: Square
"""


class Square:
    """
    This class defines a square based on 2-square

    **Task parameters:**
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)

    Public instance method: def area(self): returns current square area
    You are not allowed to import any module

    **Functions**
    __init__(self, size)
    area(self)

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

    def area(self):
        """
        public instance to return square area

        same arguments

        return:
        area of a square(int)

        """
        return(self.__size * self.__size)
