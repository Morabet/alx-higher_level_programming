#!/usr/bin/python3
"""Defining the '5-save_to_json_file' module"""

import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file, using
    a JSON representation a function that writes an Object
    to a text file, using a JSON representation
    """
    with open(filename, "w") as file:

        json.dump(my_obj, file)
