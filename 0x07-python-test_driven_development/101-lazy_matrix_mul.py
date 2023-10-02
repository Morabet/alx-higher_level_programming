#!/usr/bin/python3
"""Defining '101-lazy_matrix_mul.py'module"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices (lists of ints/floats).
    Args:
        m_a: the first Matrixlist.
        m_b: The second Matrix.
    """

    return (np.matmul(m_a, m_b))
