#!/usr/bin/python3
import json
"""
This is module 8-load_from_json_file

This module contains one function `load_from_json_file`
"""


def load_from_json_file(filename):
    """
    Write a function that creates an Object from a "JSON file"

    You must use the with statement
    don't need to manage exceptions
    if the JSON string doesn't represent an object.
    You don't need to manage file permissions / exceptions.

    Args:
    filename
    """
    with open(filename, encoding='utf-8') as my_file:
        return json.load(my_file)
