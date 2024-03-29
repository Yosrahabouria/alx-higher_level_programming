#!/usr/bin/python3
""" a Python script that displays the boddy to response"""
import urllib.request
import sys


if __name__ == '__main__':
    rq = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(rq) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as er:
        print('Error code:', er.code)
