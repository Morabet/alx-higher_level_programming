#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    if value not in a_dictionary.values():
        return a_dictionary

    else:
        keys_to_remove = []

        for k, v in a_dictionary.items():
            if v == value:
                keys_to_remove.append(k)

        for k in keys_to_remove:
            if k in a_dictionary:
                del a_dictionary[k]

        return a_dictionary
