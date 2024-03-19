#!/usr/bin/python3
"""Descriptin save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writing an object to text file function"""
    with open(filename, "w", encoding='UTF-8') as f:
        json.dump(my_obj, f)
