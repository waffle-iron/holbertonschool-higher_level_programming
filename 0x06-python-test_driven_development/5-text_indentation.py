#!/usr/bin/python3
"""
This module "5-text_indentation" is task 4
for 0x06-python-test_driven_development and
completed for Holberton School coursework.

This module supplies one function: text_indentation().

To test, run: `python3 -m doctest ./tests/5-text_indentation.txt`
"""


def text_indentation(text):
    """
    prints to stdout text with 2 new lines after certain characters

    Arguments:
    text: must be a string
    """
    if len(text) < 0 or text is None or not isinstance(text, str):
        raise TypeError('text must be a string')
    # replace chars with placeholder
    text = text.replace('.', '.\\')
    # print(text)
    text = text.replace('?', '?\\')
    # print(text)
    text = text.replace(':', ':\\')
    # print(text)
    # split string by placeholder
    # strip leading/trailing characters
    # join strings with two newlines
    print('\n\n'.join([t.strip() for t in text.split('\\')]), end="")
