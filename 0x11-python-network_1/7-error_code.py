#!/usr/bin/python3
"""
    this script takes a url , sends a req to the url
    if HTTPS status code is >= 400, print Error code: r.status_code
    otherwise display the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))
