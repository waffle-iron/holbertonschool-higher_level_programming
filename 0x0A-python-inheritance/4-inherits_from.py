#!/usr/bin/python3
"""
This is module 4-inherits_from

This module contains one function
"""


def inherits_from(obj, a_class):
    """
    checks instance of a specified class

    Args:
    obj - object
    a_class - specified class

    Returns:
    True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ;
    otherwise False.
    """
    return issubclass(a_class, a_class)
