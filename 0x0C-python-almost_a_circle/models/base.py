#!/usr/bin/python3
"""base of classes"""


class Base:
    """description of bases in the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialisation"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
