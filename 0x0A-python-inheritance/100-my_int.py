#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
