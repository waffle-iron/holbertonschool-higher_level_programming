#!/usr/bin/python3
"""
This module is task 3 for 0x06-python-test_driven_development

This module supplies one function: `say_my_name`

To test, a text file is provided in the /tests directory. To run:
`python3 -m doctest -v ./tests/3-say_my_name.txt`
"""
def say_my_name(first_name, last_name=""):
    """
    This function prints "My name is " followed by arguments

    Arguments:
    first_name: must be string
    last_name: must be string
    """
    if not isinstance(first_name, str):
        hey
    if not isinstance(last_name, str):
        hey
    else:
        print("{:s} {:s} {:s}".format("My name is ", first_name, last_name))
