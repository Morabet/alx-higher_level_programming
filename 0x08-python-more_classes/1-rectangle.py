#!/usr/bin/python3
"""defining '1-rectangle' module"""


class Rectangle:
    """defining the 'Rectangle' class"""

    def __init__(self, width=0, height=0):
        """Defining the 'width' and 'heght values"""

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """getter for the width attr"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width attr
        Raises:
            TypeError: if value not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """getter for the height attr"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height attr
        Raises:
            TypeError: if value not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
