#!/usr/bin/python3
"""Defining the '11-student' module"""


class Student:
    """Defining the student class"""

    def __init__(self, first_name, last_name, age):
        """Initialise the student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        attributes that exist in the attrs list of string
        """

        if type(attrs) is list and all(type(i) is str for i in attrs):

            my_dict = {}
            for k, v in vars(self).items():
                if k in attrs:
                    my_dict.update({k: v})

            return my_dict
        else:
            return vars(self)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        for k, v in json.items():
            if k in vars(self):
                setattr(self, k, v)
