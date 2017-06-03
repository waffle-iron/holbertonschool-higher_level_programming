#!/usr/bin/python3
"""
This is module 12-student

This module contains one class:
     `Student`

This module contains one function:
     `to_json`
"""


class Student:
    """
    Public instance attributes:
        first_name
        last_name
        age

    Public class method
    def to_json(self)
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age:
            `def __init__(self, first_name, last_name, age)`
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public class method
        def to_json(self, attrs=None): retrieves a dictionary
        representation of a Student instance
        (same as 10-class_to_json.py):

        If attrs is a list of strings, only attributes name contain
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        for item in attrs:
            try:
                dict_keys = {}
                dict_keys = getattr(self, item, None)
                return (dict_keys)
            except AttributeError:
                return (self.__dict__)
