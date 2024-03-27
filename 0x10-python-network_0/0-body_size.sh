#!/bin/bash
# sends a request to a url and displays the size of the response
curl -s "$1" | wc -c
