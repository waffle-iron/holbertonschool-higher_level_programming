#!/usr/bin/python3
"""
This module "2-matrix_divided" is task 1
for 0x06-python-test_driven_development and
completed for Holberton School coursework.

This module supplies one function: matrix_divided().

To test, run: `python3 -m doctest -v ./tests/2-matrix_divided.txt`
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix

    Arguments:
    matrix: must be a list of lists of integers or floats
    div: must be a number (integer or float)

    Return:
    matrix / div
    """
    error_type = "matrix must be a matrix (list of lists) of integers/floats"
    type_error_size = "Each row of the matrix must have the same size"
    type_error_div = "div must be a number"
    zero_error = "division by zero"
    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(error_type)
    if not all(isinstance(item, list) for item in matrix):
        raise TypeEror(error_type)
    if len(matrix[0]) == 0:
        raise TypeError(error_type)
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
    matrix_quotient = [[round(item / div, 2)
                        for item in row] for row in matrix]
    return(matrix_quotient)
