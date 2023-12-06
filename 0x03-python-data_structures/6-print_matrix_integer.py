#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Parameters:
        - matrix (List[List[int]]): 2D list representing the matrix.
    """
    for m in range(len(matrix)):
        for i in range(len(matrix[m])):
            print("{:d}".format(matrix[m][i]), end="")
            if i != (len(matrix[m]) - 1):
                print("", end="")
        print("")
