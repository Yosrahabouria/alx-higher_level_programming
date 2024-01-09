#!/usr/bin/python3
"""description for Rectangle Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class inherts from Rectangle"""
    def __init__(self, size):
        """instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return self.__size ** 2

    def __str__(self):
        """description of square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
