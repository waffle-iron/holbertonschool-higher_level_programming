#!/usr/bin/python3
"""
This module is task 1 for 0x06-python-test_driven_development

This module supplies one function: matrix_divided

To test, a text file is provided in the /tests directory. To run:
`python3 -m doctest -v ./tests/0-matrix_divided.txt`
"""
def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix

    Arguments:
    matrix: must be a list of lists of integers or floats
    div: must be a number (integer or float)

    Return:
    matrix / div or raise error if following encountered:
    - raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
    - raise a TypeError exception with the message Each row of the matrix must have the same size
    - raise a TypeError exception with the message div must be a number
    - raise a ZeroDivisionError exception with the message division by zero
    """
    type_error_type = "matrix must be a matrix (list of lists) of integers/floats"
    type_error_size = "Each row of the matrix must have the same size"
    type_error_div = "div must be a number" 
    zero_error = "division by zero"
    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(type_error_type)
    if not all(isinstance(item, list) for item in matrix):
        raise TypeEror(type_error_type)
    if len(matrix[0]) == 0:
        raise TypeError(type_error_type)
    if not isinstance(div, (int, float)):
        raise TypeError(type_error_div)
    if div == 0:
        raise ZeroDivisionError(zero_error)
    matrix_quotient = []
    for row in matrix:
        item = 0
        if len(row) != len(matrix[0]):
            raise TypeError(type_error_size)
        for item in row:
            if isinstance(item, (int, float)):
                item = int(item)
            else:
                raise TypeError(type_error_type)
            item = round(item / div, 2)
            matrix_quotient.append(item)
        matrix_quotient.append(row)
        return (matrix_quotient)
