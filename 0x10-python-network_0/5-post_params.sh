#!/bin/bash
# sends a post req to a url with a pair of variables and values
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
