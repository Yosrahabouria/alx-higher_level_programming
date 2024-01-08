#!/usr/bin/python3
"""Module for Rectangle class."""
BaseGeometry = __import__(7-base_geometry.py).BaseGeometry


class Rectangle(BaseGeometry):
    """class inherts from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
