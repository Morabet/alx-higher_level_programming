#!/usr/bin/python3
"""A script that takes in a URL, sends a request and display the value
in the X-Request-Id variable found in the header"""

if __name__ == "__main__":

    import urllib.request
    from sys import argv

    url = argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
