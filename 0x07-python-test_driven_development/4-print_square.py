#!/usr/bin/python3
"""define 4-print_square module"""


def print_square(size):
    """Implementing print_square function
    Args:
        size: the size of the square to print
    Raises
        TypeError: if size not an integer
        ValueError: if size < 0
        TypeError: if size float < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    print(("#" * size + "\n") * size, end="")
