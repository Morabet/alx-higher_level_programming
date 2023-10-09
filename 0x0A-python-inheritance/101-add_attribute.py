#!/usr/bin/python3
"""Defining the module of '101-add_attribute'"""


def add_attribute(obj, name, value):
    """Implementing a function that adds an attr to an objet"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
