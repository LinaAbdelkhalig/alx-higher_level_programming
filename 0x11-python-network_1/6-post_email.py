#!/usr/bin/python3
"""
    this script takes a url and an email
    sends a POST request to the url with the email as a param
    then displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    em = {'email': sys.argv[2]}
    r = requests.post(url, data=em)
    print(r)
