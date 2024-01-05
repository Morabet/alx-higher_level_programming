#!/usr/bin/python3



def find_peak(list_of_integers):

    n = len(list_of_integers)

    if (n == 0):
        return None

    if n == 1:
        return list_of_integers[0]
    elif list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[n - 1] >= list_of_integers[n - 2]:
        return list_of_integers[n - 1]

    for i in range(1, n - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]

