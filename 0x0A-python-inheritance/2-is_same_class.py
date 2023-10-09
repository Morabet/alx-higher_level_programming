#!/usr/bin/python3
""" define 2-is_same_class module """


def is_same_class(obj, a_class):
    """Return true if object is an instance of the class or false """

    return type(obj) is a_class
