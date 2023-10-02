#!/usr/bin/python3
"""defining the '100-matrix_mul.py' module"""


def matrix_mul(m_a, m_b):
    """defining the 'matrix_mul' function for matrix multiplication
    Args:
        m_a: Matrix A
        m_b: Matrix B
    Raises:
        TypeError: if m_a or m_b is not a list.
        TypeError: if m_a or m_b is not a list of lists.
        ValueError: if m_a or m_b is empty (it means: = [] or = [[]]).
        TypeError: if element of list of lists is not an integer or a float.
        TypeError: if not all ‘rows’ should of the same size.
        ValueError: If m_a and m_b can’t be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for i in row:
            if (not isinstance(i, int)) and (not isinstance(i, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for i in row:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = []

    for i in range(len(m_a)):
        m_c = []
        for j in range(len(m_b[0])):
            x = 0

            for k in range(len(m_b)):

                x += m_a[i][k] * m_b[k][j]

            m_c.append(x)

        matrix.append(m_c)

    return matrix
