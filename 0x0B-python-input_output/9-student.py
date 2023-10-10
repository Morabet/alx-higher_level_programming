#!/usr/bin/python3
"""Defining the '9-student' module"""


class Student:
    """Defining the student class"""

    def __init__(self, first_name, last_name, age):
        """Initialise the student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves a dictionary representation of a Student instance
        """

        return vars(self)
