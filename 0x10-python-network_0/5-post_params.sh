#!/bin/bash
#takes in a URL, sends a POST request to the passed URL,
#and displays the body of the response
<<<<<<< HEAD
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
=======
email="test@gmail.com"
subject="I will always be here for PLD"
curl -sX POST -d "email=$email" -d "subject=$subject" "$1"
>>>>>>> 9290a1d97087a133ae480a2eca733518e27837d8
