#!/usr/bin/python3
"""Defining the '12-pascal_triangle' module"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    tri_pascal = [[1]]
    while len(tri_pascal) != n:
        tri = tri_pascal[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tri_pascal.append(tmp)
    return tri_pascal
