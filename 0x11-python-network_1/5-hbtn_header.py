#!/usr/bin/python3
""" python script"""
import requests
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    r = requests.get(URL)
    print(r.headers.get('X-Request-Id'))
