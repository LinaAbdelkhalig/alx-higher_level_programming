#!/usr/bin/python3
""" 
    this script senda req and displays the body of the resp in utf-8
    it also handles the urllib.error.HTTPError exception
"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            print("{}".format(page.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
