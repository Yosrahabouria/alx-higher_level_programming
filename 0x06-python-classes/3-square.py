#!/usr/bin/python3
"""Square Functions"""


class Square:
    """Square Defintion."""

    def __init__(self, size=0):
        """ Instantiation with optional size.

        Args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculate Area of Square.

        Returns: the current square area.
        """
        return self.__size ** 2
