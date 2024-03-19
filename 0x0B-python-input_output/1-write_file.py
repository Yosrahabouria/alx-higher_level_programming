#!/usr/bin/python3
"""Descriptin write_file function"""


def write_file(filename="", text=""):
    """writing file function"""
    with open(filename, "w", encoding='UTF-8') as f:
        return f.write(text)
