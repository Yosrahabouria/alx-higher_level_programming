#!/usr/bin/python3
"""Python script """
import requests
import sys


if __name__ == '__main__':
    rs = requests.get(sys.argv[1])
    if rs.status_code >= 400:
        print('Error code:', rs.status_code)
    else:
        print(rs.text)
