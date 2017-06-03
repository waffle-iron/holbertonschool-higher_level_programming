#!/usr/bin/python3
import json
"""
This is module 7-save_to_json_file

This module contains one function `save_to_json_file`
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes Object to text file,
    using a JSON representation:
    You must use the with statement
    You don't need to manage exceptions if the object can't be serialized.
    You don't need to manage file permission exceptions.

    Args:
    my_obj
    filename
    """
    with open(filename, 'w') as my_file:
        my_file.write(json.dumps(my_obj))
