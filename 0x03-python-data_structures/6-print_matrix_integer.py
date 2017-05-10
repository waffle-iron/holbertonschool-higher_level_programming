#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:  # check if matrix exists
        return None

    if len(matrix[0]) == 0:  # check length of matrix
        return

    for row in range(0, len(matrix[:])):  # iterate through matrix and print ints
        for idx in matrix[row]:
            print("{:d}".format(idx), end="")
            row_size = len(matrix[row]) - 1
            row_index = matrix[row].index(idx)
            if row_index != row_size:  # check that row index not equal to size of row
                print(' ', end="")  # print spaces between numbers
            else:
                print()  # insert new line once index equals size of row
        print()
