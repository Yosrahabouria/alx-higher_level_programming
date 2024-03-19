#!/usr/bin/python3
"""description of class inhertin"""


class MyInt(int):
    """inherting from int"""
    def __new__(cls, *args, **kwargs):
        """creation of class copie"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, compared_point):
        """comparing function"""
        return int(self) != compared_point

    def __ne__(self, compared_point):
        """comparing function"""
        return int(self) == compared_point
