#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """getter for the size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter for the size attribute"""

        self.__init__(value)

    def area(self):
        """
        Calculate area of the square
        Returns: The the area of the square
        """
        return self.__size ** 2

    def __eq__(self, other):
        """ovveride '==' function"""

        return self.area() == other.area()

    def __ne__(self, other):
        """ovveride '!=' function"""

        return self.area() != other.area()

    def __gt__(self, other):
        """ovveride '>' function"""

        return self.area() > other.area()

    def __ge__(self, other):
        """ovveride '>=' function"""

        return self.area() >= other.area()

    def __lt__(self, other):
        """ovveride '<' function"""

        return self.area() < other.area()

    def __le__(self, other):
        """ovveride '<=' function"""

        return self.area() <= other.area()
