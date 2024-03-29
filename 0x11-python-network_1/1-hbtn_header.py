#!/usr/bin/python3
""" python script """
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])
