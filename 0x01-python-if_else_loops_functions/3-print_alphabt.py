#!/usr/bin/python3

for ch in range(ord('a'), ord('z') + 1):
    if ch != ord('q') and ch != ord('e'):
        print("{}".format(chr(ch)), end="")
