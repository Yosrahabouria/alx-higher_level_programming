#!/usr/bin/python3
"""defines class student"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """initialisation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a student"""
        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    dic[key] = value
        return dic
