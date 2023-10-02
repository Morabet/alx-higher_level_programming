#!/usr/bin/python3
"""define '3-say_my_name' module """


def say_my_name(first_name, last_name=""):
    """Implementing say_my_name function:
    Args:
        first_name: first string
        last_name: second string
    Raises:
        TypeError: if either one of the args not string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
