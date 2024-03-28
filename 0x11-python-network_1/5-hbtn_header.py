#!/usr/bin/python3
"""
    this script takes in a url and sends it a request
    it then displays the value of the X-Request-Id variable
    found in the header of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print("{}".format(r.headers.get('X-Request-Id')))
