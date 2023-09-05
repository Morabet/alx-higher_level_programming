#!/usr/bin/python3

def uppercase(str):

    for c in str:
        x = ord(c) in range(ord('a'), ord('z') + 1)
         print("{}".format(chr(ord(c) - ord(' ')) if x else c), end="")
    else:
        print()
