#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except BaseException as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return None
