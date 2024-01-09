#!/usr/bin/python3
"""Descriptin read_file function"""


def read_file(filename=""):
    """reading file function"""
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
