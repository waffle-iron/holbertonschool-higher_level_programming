#!/usr/bin/python3
"""
This is module 11-student

This module contains one class:
     `Student`

This module contains one function:
     `to_json`
"""


class Student():
    """
    Public instance attributes:
        first_name
        last_name
        age

    Instantiation with first_name, last_name and age:
    `def __init__(self, first_name, last_name, age)`

    Public class method
    def to_json(self): retrieves a dictionary representation
    of a Student instance (same as 10-class_to_json.py)
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (self.__dict__)
