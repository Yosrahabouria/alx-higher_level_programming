#!/bin/bash
# Takes in a URL, sends request and displays the size of the response
curl -sw '%{size_download}\n' -o /dev/null "$1"
