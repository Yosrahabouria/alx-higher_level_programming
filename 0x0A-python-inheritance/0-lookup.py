#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """function that returns the list of available.
    Args:
        obj: object of list.

    Returns:
        list: list of availables.
    """
    return dir(obj)
