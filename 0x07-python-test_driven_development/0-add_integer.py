#!/usr/bin/python3
"""define add_integer modul """


def add_integer(a, b=98):
    """define add_integer function
    Args:
        a: integer or float.
        b: integer or float.
    Raise:
        TypeError: if a or b not integer or float.

    Return:
        Sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest

    doctest.testfile('tests/0-add_integer.txt')
