#!/bin/bash
# displays all the http methods the server will accept
curl -s -X OPTIONS -I "$1" |grep Allow
