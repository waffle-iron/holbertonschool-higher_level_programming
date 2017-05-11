#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:  # check if matrix exists
        return None

    if len(matrix[:]) == 0:  # check length of matrix
        print()
        return

    for row in range(0, len(matrix=[:])):
        for idx in matrix[row]:
            print("{:d}, ".format(squareit(int),end=""))
            row_size = len(matrix[row]) -1
            row_index = matrix[row].index(idx)
            if row_index != row_size:  # check size of row_index
                print(' ', end="")  # print spaces between numbers
            else:
                print()  # insert new line once index equals size of row


