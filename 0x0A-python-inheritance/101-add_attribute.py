#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible"""


def add_attribute(obj, att, value):
    """adds a new attribute to an object
    Args:
        obj: input value
        att: input value
        value: input value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
