#!/usr/bin/python3
"""
This is module 1-my_list

This module contains one class and one public instance method
"""


class MyList(list):
    """
    inherits from `list`

    Public instance method:
    `def print_sorted(self):` that prints the list, but sorted (ascending sort)

    Args:

    Returns:
    """
    def print_sorted(self):
        list(self)
