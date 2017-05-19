#!/usr/bin/python3
"""
This module "6-square" is task 6 for 0x07-python-classes
and completed for Holberton School coursework.

This module contains one class: Square
"""


class Square:
    """
    This class defines a square based on 5-square

    **Task parameters:**
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)

    Public instance method: def area(self): returns current square area
    You are not allowed to import any module

    **Functions**
    __init__(self, size)
    area(self)
    my_print(self)

    **Example**
    my_square_1 = Square(3)
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        instantiate an object based on Square class

        Arguments:
        size must be an integer
        size must be >= 0
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        property getter def size(self) to retrieve it
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        property setter def size(self, value) to set size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        property def position(self): to retrieve it
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        property setter def position(self, value) to set position
        """
        if not isinstance(value, tuple) or all(value) < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        public instance to return square area

        return:
        area of a square(int)

        """
        return(self.__size * self.__size)
    def my_print(self):
        """
        Public instance method: def my_print(self): that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for e in range(0, self.__size):
                print("".join("{}".format("#" * self.__size)))
