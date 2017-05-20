#!/usr/bin/python3
"""
This module "8-rectangle" is task 8 for 0x08-python-more_classes and completed
for Holberton School coursework.

This module contains one class: Rectangle
"""


class Rectangle:
    """This class defines a rectangle based on 7-rectangle

    Attributes:
        number_of_instances - public, default to 0
        print_symbol - public, initialized as '#'
    Functions:
        __init__(self, width=0, height=0)
        area(self)
        perimeter(self)
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This instantiates an object based on Rectangle class
        Attributes:
            width (int): private, Defaults to 0.
            height (int): private, Defaults to 0.
        Args:
            width (int): Defaults to 0.
            height (int): Defaults to 0.
        Raises:
            ValueError: If `width` is less than 0
            TypeError: If `width` not an integer
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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
            string = ''.join((format(self.print_symbol) *
                              pubwidth + '\n') * pubheight)
            string = string[0:-1]
            return (string)

    def __repr__(self):
        """
        class method specific way to reproduce output
        """
        return("Rectangle ({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """class method specific way to delete instance
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        return: the biggest rectangle based on the area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return(rect_2)

    @classmethod
    def square(cls, size=0):
        """classmethod to create a square
        Args:
            cls (int)
            size (int): Defaults to 0.
        Return: a new Rectangle instance with width == height == size
        """
        return (cls(size, size))
