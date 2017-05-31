#!/usr/bin/python3
import json
"""
This is module 6-from_json_string

This module contains one function `from_json_string`
"""

def from_json_string(my_str):
    """
    Write a function that returns an object (Python data structure) represented by a JSON string:
    You don't need to manage exceptions if the JSON string doesn't represent an object.

    Args:
    my_str

    Return:
    object represented by a JSON string
    """
    return json.loads(my_str)
