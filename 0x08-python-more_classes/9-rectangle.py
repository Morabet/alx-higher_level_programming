#!/usr/bin/python3
"""defining '9-rectangle' module"""


class Rectangle:
    """defining the 'Rectangle' class"""

    number_of_instances = 0

    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """return the biggest rectangle"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance"""

        return Rectangle(size, size)

    def __init__(self, width=0, height=0):
        """Defining the 'width' and 'heght values"""

        Rectangle.number_of_instances += 1

        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")
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
            s += f"{self.print_symbol}" * self.width

            if i != self.height - 1:
                s += "\n"

        return s

    def __repr__(self):
        """ return the instance string representation"""

        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """print message when deleting instance"""

        Rectangle.number_of_instances -= 1

        print("Bye rectangle...")
