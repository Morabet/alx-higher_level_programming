#!/usr/bin/python3
"""Defining the '100-append_after' module"""


def append_after(filename="", search_string="", new_string=""):
    """
    a function that inserts a line of text to a file,
    after each line containing a specific string
    """

    lines = []

    with open(filename, "r+") as file:

        lines = file.readlines()

    index = 0
    for i in lines:
        if search_string in i:
            lines.insert(index + 1, new_string)
        index += 1

    text = "".join(lines)

    with open(filename, "w") as file:
        file.write(text)
