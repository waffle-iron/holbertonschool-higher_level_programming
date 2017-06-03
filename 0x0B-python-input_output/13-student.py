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
        if attrs is None:
            return (self.__dict__)
        else:
            dict_keys = {}
            for item in attrs:
                if hasattr(self, item):
                    dict_keys[item] = getattr(self, item)
            return (dict_keys)
    def reload_from_json(self, json):
        """public class method
        Replaces all attributes of the Student instance:
                 You can assume json will always be a dictionary
                 A dictionary key will be the public attribute name
                 A dictionary value will be the value of the public attribute
        """
        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]
