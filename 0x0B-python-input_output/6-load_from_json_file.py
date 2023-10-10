#!/usr/bin/python3
"""Defining the '6-load_from_json_file' module"""

import json


def load_from_json_file(filename):
    """
    def load_from_json_file(filename).
    """

    with open(filename, "r") as file:

        return json.load(file)
