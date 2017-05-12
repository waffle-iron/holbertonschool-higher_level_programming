#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:  # check if matrix exists
        return None
    if matrix == []:  # return if matrix is empty
        return
    matrix_squared = [[x*x for x in row] for row in matrix]
    return (matrix_squared)
