#!/usr/bin/python3
"""a Python script that takes 2 arguments to solve the
challenge"""
import requests
import sys

if __name__ == '__main__':
    URL = 'https://api.github.com/repos/' + sys.argv[2] + '/' + sys.argv[1] + \
          '/commits'
    rs = requests.get(URL)
    try:
        for j in range(10):
            print('{}: {}'.format(rs.json()[j]['sha'],
                                  rs.json()[j]['commit']['author']['name']))
    except:
        pass
