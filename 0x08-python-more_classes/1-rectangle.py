#!/usr/bin/python3
"""
This module "1-rectangle" is task 1 for 0x08-python-more_classes and completed
for Holberton School coursework.

This module contains one class: Rectangle
"""


class Rectangle:
    """This class defines a rectangle based on 0-rectangle

    Attributes:
        width - private instance 
        height - private instance
    Functions:
        __init__(self, width=0, height=0)
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
