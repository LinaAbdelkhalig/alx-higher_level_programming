#!/bin/bash
# send a request to 0.0.0.0:5000/catch_me that causes the server to respond with YOU got Me !
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
