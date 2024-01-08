#!/usr/bin/python3
"""Module for BaseGeometry method."""


class BaseGeometry:
    """a BaseGeometry empty class"""
    def area(self):
        """raise exception when message appear"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """to validate variable"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
