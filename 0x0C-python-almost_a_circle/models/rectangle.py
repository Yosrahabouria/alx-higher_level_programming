#!/usr/bin/python3
""" class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Class rectangle"""

    def __init__(self, width, height, pos_x=0, pos_y=0, id=None):
        """Initialization"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

    @property
    def width(self):
        """Return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation"""
        if type(value) == int:
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation"""
        if type(value) == int:
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def pos_x(self):
        """Return x position"""
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, value):
        """Set x position with validation"""
        if type(value) == int:
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__pos_x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def pos_y(self):
        """Return y position"""
        return self.__pos_y

    @pos_y.setter
    def pos_y(self, value):
        """Set y position with validation"""
        if type(value) == int:
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__pos_y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """Calculate area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Print the Rectangle with '#' characters"""
        for _ in range(self.__pos_y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__pos_x + '#' * self.__width)

    def __str__(self):
        """Return a string representation of the class Rectangle instance"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.pos_x, self.pos_y,
                                                 self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign values to attributes"""
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.pos_x = arg
                elif i == 4:
                    self.pos_y = arg
        if kwargs is not None and len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    def to_dictionary(self):
        """Return dictionary description of the instance of class Rectangle"""
        keys = ["id", "width", "height", "pos_x", "pos_y"]
        return {a: getattr(self, a) for a in keys}
