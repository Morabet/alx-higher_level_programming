#!/usr/bin/python3
"""defining '5-rectangle' module"""


class Rectangle:
    """defining the 'Rectangle' class"""

    def __init__(self, width=0, height=0):
        """Defining the 'width' and 'heght values"""

        self.__width = width
        self.__height = height

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

    def area(self):
        """Implementing the area method
            Returns: the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """Implementing the perimeter method
            Returns: the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """ return the rectangle in '#'"""

        if self.width == 0 or self.height == 0:
            return ""

        s = ""
        for i in range(self.height):
            s += "#" * self.width

            if i != self.height - 1:
                s += "\n"

        return s

    def __repr__(self):
        """ return the instance string representation"""

        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """print message when deleting instance"""

        print("Bye rectangle...")
