#!/usr/bin/python3
""" 
    this script takes in a url and sends it a request
    it then displays the value of the X-Request-Id variable
    found in the header of the response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print("{}".format(headers['X-Request-Id']))
