#!/usr/bin/python3
"""Implementing the '7-add_item' script:
    that adds all arguments to a Python list,
    and then save them to a file
"""

from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = argv[1:]
file = "add_item.json"

try:
    old_list = load_from_json_file(file)

except FileNotFoundError:
    old_list = []

old_list.extend(args)

save_to_json_file(old_list, file)
