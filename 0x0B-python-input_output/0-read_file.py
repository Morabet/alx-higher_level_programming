#!/usr/bin/python3
"""Defining the '0-read_file' module"""


def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, encoding="utf-8") as file:
        text = file.read()

        print(text, end="")
