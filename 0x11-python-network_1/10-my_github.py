#!/usr/bin/python3
"""Python script"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    URL = 'https://api.github.com/user'
    rs = requests.get(URL, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    rs = requests.get(URL, auth=(sys.argv[1], sys.argv[2]))
    try:
        print(rs.json()['id'])
    except:
        print('None')
