#!/usr/bin/python3
"""
This is module 1-my_list

This module contains one class and one public instance method
"""


class MyList(list):
    """
    inherits from `list`

    Public instance method:
    `def print_sorted(self):` 

    Args:

    Returns:
    """
    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(set(self))
