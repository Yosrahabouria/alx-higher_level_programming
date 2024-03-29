#!/usr/bin/python3
"""python scriptt"""
import requests


if __name__ == "__main__":
    URL = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(URL)
    info = r.text
    result_Type = type(info)
    print(f'Body response:\n\t- type: {result_Type}\n\t\
- content: {info}')
