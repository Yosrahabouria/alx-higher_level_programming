#!/usr/bin/python3
""" Python script """
import requests
import sys

if __name__ == '__main__':
    rs = requests.post(sys.argv[1], info={'email': sys.argv[2]})
    print(rs.text)
