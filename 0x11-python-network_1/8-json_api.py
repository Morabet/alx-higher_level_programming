#!/usr/bin/python3
"""Takes in a letter and sends a POST request
to a url with the letter as a parameter."""

if __name__ == "__main__":

    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'
    letter = {'q': argv[1]} if len(argv) > 1 else {'q': ""}
    try:
        r = requests.post(url, data=letter)
        result = r.json()
        if (result):
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
