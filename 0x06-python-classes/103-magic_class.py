#!/usr/bin/python3
"""define module"""
import math


class MagicClass:
    """define magic class"""

    def __init__(self, radius=0):
        """Instantiate the radius arg """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculate area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculate circumference"""
        return 2 * math.pi * self.__radius
