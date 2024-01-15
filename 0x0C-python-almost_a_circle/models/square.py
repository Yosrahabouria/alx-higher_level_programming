#!/usr/bin/python3
"""definition of the class Square"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """class Square inherits from class Rectangle"""
    def __init__(self, size, pos_x=0, pos_y=0, ident=None):
        """Initialization"""
        super().__init__(size, size, pos_x, pos_y, ident)

    @property
    def size(self):
        """return size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("size must be > 0")
            self.width = value
            self.height = value
        else:
            raise TypeError("size must be an integer")

    def __str__(self):
        """string description of an instance of class Square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.ident,
                                             self.pos_x, self.pos_y, self.width)

    def update(self, *args, **kwargs):
        """Assigns argument to attribute
        Args:
            args: input value
            kwargs: input value
        """
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.ident = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.pos_x = arg
                elif i == 3:
                    self.pos_y = arg
        if kwargs is not None and len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """dictionary description of instance of class Square"""
        keys = ["ident", "size", "pos_x", "pos_y"]
        return {a: getattr(self, a) for a in keys}
