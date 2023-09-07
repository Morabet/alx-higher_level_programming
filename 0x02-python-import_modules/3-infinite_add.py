#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    sum = 0

    if len(argv) > 1:

        for arg in argv[1:]:
            sum += int(arg)

    print(sum)
