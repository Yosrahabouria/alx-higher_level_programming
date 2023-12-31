#!/usr/bin/python3
""" class Rectangle that defines a rectangle
"""


class Rectangle:
    """Definition of a rectangle"""
    def __init__(self, width=0, height=0):
        """intialization of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """set it"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """set it"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
