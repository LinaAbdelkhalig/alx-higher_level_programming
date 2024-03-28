#!/bin/bash
# displays all the http methods the server will accept
curl -sI -X OPTIONS "$1" | grep Allow: | cut -d' ' -f2-
