#!/bin/bash
# take a url and send a get to the url and display tho body of 200 resp
curl -s -L -w "%{http_code}" "$1" | grep -q "200$" && curl -s -L "$1"
