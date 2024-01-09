#!/usr/bin/python3
"""Descriptin append_write function"""


def append_write(filename="", text=""):
    """appending file function"""
    with open(filename, "a", encoding='UTF-8') as f:
        return f.write(text)
