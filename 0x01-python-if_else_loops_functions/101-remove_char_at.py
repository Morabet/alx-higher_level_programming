#!/usr/bin/python3

def remove_char_at(str, n):

    new_str = ""
    j = 0

    for i in str:
        if j != n:
            new_str += i
        j += 1

    return new_str
