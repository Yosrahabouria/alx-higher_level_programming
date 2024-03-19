#!/usr/bin/python3
"""Descriptin load_from_json_file function"""


import json


def load_from_json_file(filename):
    """creating an object from json file function"""
    with open(filename, "r", encoding='UTF-8') as f:
        return json.load(f)
