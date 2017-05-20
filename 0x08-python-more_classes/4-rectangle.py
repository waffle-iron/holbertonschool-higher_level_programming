#!/usr/bin/python3
"""
This module "4-rectangle" is task 4 for 0x08-python-more_classes and completed
for Holberton School coursework.

This module contains one class: Rectangle
"""


class Rectangle:
    """This class defines a rectangle based on 3-rectangle

    Attributes:
        width - private instance
        height - private instance
    Functions:
        __init__(self, width=0, height=0)
        area(self)
        perimeter(self)
    """

    def __init__(self, width=0, height=0):
        """This instantiates an object based on Rectangle class
        Args:
            width (int): Defaults to 0.
            height (int): Defaults to 0.
        Raises:
            ValueError: If `width` is less than 0
            TypeError: If `width` not an integer
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        retrieves width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        sets value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        retrieves height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        sets value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """public instance method
        Returns:
                rectangle area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """public instance method
        Returns:
                rectangle perimeter
                if width or height is equal to 0, perimeter is equal to 0
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """
        class method specific way for string output
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            pubheight = self.__height
            pubwidth = self.__width
            string = ''.join(('#' * pubwidth + '\n') * pubheight)
            string = string[0:-1]
            return (string)

    def __repr__(self):
        """
        class method specific way to reproduce output
        """
        return("Rectangle ({:d}, {:d})".format(self.__width, self.__height))
