#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":

    import requests

    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
