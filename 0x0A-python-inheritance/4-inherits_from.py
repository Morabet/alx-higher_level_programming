#!/usr/bin/python3
""" define 4-inherits_from module """


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that inherited
        from a_class
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
