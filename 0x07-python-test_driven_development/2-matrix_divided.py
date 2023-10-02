#!/usr/bin/python3
"""define matrix divided module"""


def matrix_divided(matrix, div):
    """Implementing matrix_divided function
    Args:
        matrix: a list of lists
        div: the division number.
    Raises:
        TypeError: must be list of list of integers or floats.
        TypeError: matrix's rows must be of the same size.
        TypeError: div must be an integer or float.
        ZeroDivisionError: if div == 0
    """

    err_text = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or matrix == [] or \
            not all(isinstance(row, list) for row in matrix):

        raise TypeError(err_text)

    for row in matrix:
        for i in row:
            if (not isinstance(i, int)) and (not isinstance(i, float)):
                raise TypeError(err_text)

    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
