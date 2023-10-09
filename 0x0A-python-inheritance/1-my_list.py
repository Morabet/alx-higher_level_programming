#!/usr/bin/python3
""" define 1-my_list module """


class MyList(list):
    """ define MyList class """

    def print_sorted(self):
        """ sorted list """
        print(sorted(self))
