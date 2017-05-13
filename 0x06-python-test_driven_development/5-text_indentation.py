#!/usr/bin/python3
"""
This module is task 4 for 0x06-python-test_driven_development

This module supplies one function: `text_indentation`

To test, a text file is provided in the /tests directory. To run:
`python3 -m doctest ./tests/5-text_indentation.txt`
"""
def text_indentation(text):
    """
    prints to stdout text from argument with 2 new lines after specific characters

    Arguments:
    text: must be a string
    """
    if len(text) < 0 or text is None or not isinstance(text, str):
        raise TypeError('text must be a string')
    # replace chars with placeholder
    text = text.replace('.',r'\\')
    print(text)
    print('\n'.join([t.strip() for t in text.split('\\')]), end="")
