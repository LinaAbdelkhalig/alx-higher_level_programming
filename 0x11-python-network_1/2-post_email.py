#!/usr/bin/python3
"""
    this script takes in url and email and sends a POST req to the url
    with the email as paramaeter
    and then displays the body of the response
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print("{}".format(page.decode('utf-8')))
