#!/usr/bin/python3
"""
This is module 9-add_item

This module contains one function `add_item`
"""

import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def add_item(filename, args):
    """
    script that adds all args to a Python list,
    and then saves them to a file
    *must use your function
    save_to_json_file from 7-save_to_json_file.py
    *must use your function
    load_from_json_file from 8-load_from_json_file.py
    list must be saved as a JSON representation
    in a file named add_item.json
    If the file doesn't exist, it should be created
    You don't need to manage file permissions / exceptions.

    Args:
    filename
    args
    """
    try:
        my_obj = load_from_json_file(filename)
    except FileNotFoundError:
        my_obj = []
    save_to_json_file(my_obj + args, filename)

    if __name__ == "__main__":
        filename = "add_item.json"
        load_and_save(filename, sys.argv[1:])
