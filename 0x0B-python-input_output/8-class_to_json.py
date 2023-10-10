#!/usr/bin/python3
"""Defining the '8-class_to_json' module"""


def class_to_json(obj):
    """ a function that returns the dictionary description
    with simple data structure for JSON serialization of an object
    """

    return vars(obj)
