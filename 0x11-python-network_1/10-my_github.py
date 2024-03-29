#!/usr/bin/python3
"""
    this script takes github username and password
    and uses github api to display the id of the user
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    print("{}".format(response.json().get('id')))
