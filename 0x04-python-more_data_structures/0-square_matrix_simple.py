#!/usr/bin/python3
"""
    Prints a matrix of integers.

    Parameters:
        - matrix (List[List[int]]): 2D list representing the matrix.
    """
def square_matrix_simple(matrix=[]):
    newmatrix = [[i ** 2 for i in row] for row in matrix]
    return newmatrix
