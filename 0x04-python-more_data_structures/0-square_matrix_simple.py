#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Calculates the square of each element in the given matrix.

    Args:
        matrix (list of lists): The matrix whose elements are to be squared.

    Returns:
        list of lists: The matrix with each element squared.
    """
    squared_matrix = []
    for row in matrix:
        squared_row = [x ** 2 for x in row]
        squared_matrix.append(squared_row)
    return squared_matrix
