#!/usr/bin/python3
""" defines a square"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """Instantiation with optional size.


        Args:
            size: size of square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
