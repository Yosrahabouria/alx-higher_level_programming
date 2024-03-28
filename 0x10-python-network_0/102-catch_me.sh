#!/bin/bash
#makes a request to 0.0.0.0:5000/catch_me that causes the server
curl -sLX PUT -H "Origin:School" -d "user_id=98" "0.0.0.0:5000/catch_me"
