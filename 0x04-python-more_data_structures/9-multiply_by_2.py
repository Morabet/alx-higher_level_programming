#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    return {key: (lambda x: x * 2)(value)
            for key, value in a_dictionary.items()}
