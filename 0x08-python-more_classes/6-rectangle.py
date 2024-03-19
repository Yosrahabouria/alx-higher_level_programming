#!/usr/bin/python3
""" class Rectangle that defines a rectangle
"""


class Rectangle:
    """Definition of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """intialization of rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """return string"""
        str1 = ""
        if self.__width != 0 and self.__height != 0:
            str1 += "\n".join("#" * self.__width
                              for a in range(self.__height))
        return str1

    def __repr__(self):
        """return string representation of rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print message when instance of rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
