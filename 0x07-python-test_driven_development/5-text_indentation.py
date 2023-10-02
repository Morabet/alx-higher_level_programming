#!/usr/bin/python3
"""Difining the '5-text_indentation' module"""


def text_indentation(text):
    """Implementing the text_indentation function
        function prints a text with 2 new lines after each
        of these characters: '.', '?' and ':'
    Args:
        text: as string
    Raises:
        TypeError: if text not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sep = ['.', '?', ':']

    i = 0

    while i < len(text) and text[i] == " ":
        i += 1

    while i < len(text):
        print(text[i], end="")

        if text[i] == "\n" or text[i] in sep:
            if text[i] in sep:
                print("\n")

            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
