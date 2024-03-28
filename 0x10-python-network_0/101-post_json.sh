#!/bin/bash
# sends a JSON POST request to a url
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
