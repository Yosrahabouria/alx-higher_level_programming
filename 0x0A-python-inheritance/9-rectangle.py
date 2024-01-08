#!/usr/bin/python3
"""BaseGeometry class with inherted Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class inherts from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """string description method"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
