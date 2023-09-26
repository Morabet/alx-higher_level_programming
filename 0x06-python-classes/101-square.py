#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing this square class
        Args:
            size: represnets the size of the square defined
            position: where the coordinates in the square
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
            TypeError: if tuple is not of 2 integers < 0
        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

        if not isinstance(position, tuple) or \
                len(position) != 2 or \
                not isinstance(position[0], int) or position[0] < 0 or \
                not isinstance(position[1], int) or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position

    @property
    def size(self):
        """getter for the size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """setter for the size attribute"""
        self.__init__(value, self.__position)

    @property
    def position(self):
        """getter for the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for the position attribute"""
        self.__init__(self.__size, value)

    def area(self):
        """
        Calculate area of the square
        Returns: The the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """print the square in # """

        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                [print() for i in range(self.__position[1])]
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        """print the square in # """
        if self.__position[1] != 0:
            [print() for i in range(self.__position[1])]

        for i in range(self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")

        return ""
