#!/bin/bash
<<<<<<< HEAD
#script that sends a request to a URL passed as an argument,
=======
#script that sends a request to a URL passed as an argument
>>>>>>> 9290a1d97087a133ae480a2eca733518e27837d8
#and displays only the status code of the response
curl -s "$1" -o /dev/null -w "%{http_code}"
