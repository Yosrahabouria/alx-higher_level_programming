#!/usr/bin/python3
"""Square function"""


class Square:
    """Square Modele."""

    def __init__(self, size=0):
        """Instantiation with optional size.

        Args:
            size: size of square.
        """
        self.size = size

    @property
    def size(self):
        """
        calculate the size of side.

        Returns:
        the size of side.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """calculate size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
         """calculate of size.

         Returns:
         The size of area.
         """
         return self.__size ** 2
