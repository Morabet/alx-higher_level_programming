#!/usr/bin/python3

def roman_to_int(roman_string):

    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    values = [dict[char] for char in roman_string]
    result = 0

    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)

    if len(roman_string) == 1:
        for value in values:
            result += value

    if roman_string[0] > roman_string[-1]:
        for value in values:
            result += value

    if roman_string[0] == roman_string[-1]:
        for value in values:
            result += value

    if roman_string[0] < roman_string[-1]:
        for value in reversed(values):
            if result == 0:
                result = value
            else:
                result -= value

    return result
