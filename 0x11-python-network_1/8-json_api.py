#!/usr/bin/python3
"""
    this script takes a letter and sends a POST to
    https://0.0.0.0:5000/search_user with the letter as the parameter
"""

import requests
import sys

if __name__ == "__main__":
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""
    url = 'http://0.0.0.0:5000/search_user'
    dat = {'q': letter}
    try:
        r = requests.post(url, data=dat)
        rjson = r.json()
        if rjson:
            print("[{}] {}".format(rjson.get('id'), rjson.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
