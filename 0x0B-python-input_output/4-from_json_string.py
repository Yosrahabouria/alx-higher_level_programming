#!/usr/bin/python3
"""Descriptin from_json_string function"""


import json


def from_json_string(my_str):
    """returns the JSON presentation of an string function"""
    return json.loads(my_str)
