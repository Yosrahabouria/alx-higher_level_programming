#!/usr/bin/python3
"""definition of the class Base"""

import json
import csv


class Base:
    """Base of classes"""

    __num_objects = 0

    def __init__(self, identifier=None):
        """Initialization"""

        if identifier is not None:
            self.identifier = identifier
        else:
            type(self).__num_objects += 1
            self.identifier = type(self).__num_objects

    @staticmethod
    def to_json_string(list_dicts):
        """json string of list_dicts"""

        if list_dicts is None or len(list_dicts) == 0:
            return "[]"
        else:
            return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_objects):
        """ json string of list_objects"""
        filename = cls.__name__ + ".json"
        to_save = []
        if list_objects is None:
            with open(filename, mode="w", encoding="UTF-8") as f:
                json.dump(to_save, f)
        else:
            for obj in list_objects:
                obj = obj.to_dictionary()
                json_obj = json.loads(cls.to_json_string(obj))
                to_save.append(json_obj)
            with open(filename, mode="w", encoding="UTF-8") as f:
                json.dump(to_save, f)

    @staticmethod
    def from_json_string(json_str):
        """List of a JSON string"""
        if json_str is None or len(json_str) == 0:
            res = []
            return res
        return json.loads(json_str)

    @classmethod
    def create(cls, **dict_data):
        """Class instance with all attributes"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Square":
            temp = Square(1)
        elif cls.__name__ == "Rectangle":
            temp = Rectangle(2, 7)
        temp.update(**dict_data)
        return temp

    @classmethod
    def load_from_file(cls):
        """List of class instances"""
        filename = cls.__name__ + ".json"
        res = []

        try:
            with open(filename, encoding="UTF-8") as f:
                data = cls.from_json_string(f.read())
        except:
            return []

        for d in data:
            temp = cls.create(**d)
            res.append(temp)
        return res

    @classmethod
    def save_to_file_csv(cls, list_objects):
        """CSV of Python list_objects"""
        if list_objects is None:
            filename = str(type(cls).__name__) + ".json"
            with open(filename, mode="w", encoding="UTF-8") as f:
                f.write("[]")
        else:
            filename = str(type(list_objects[0]).__name__) + ".csv"
            with open(filename, mode="w", encoding="UTF-8") as f:
                writer = csv.writer(f)
                for obj in list_objects:
                    if str(cls.__name__) == "Rectangle":
                        writer.writerow([obj.identifier, obj.width, obj.height,
                                         obj.x, obj.y])
                    elif str(cls.__name__) == "Square":
                        writer.writerow([obj.identifier, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """List of class instances"""
        filename = str(cls.__name__) + ".csv"
        res = []
        if os.path.isfile(filename):
            with open(filename, encoding="UTF-8") as f:

                if str(cls.__name__) == "Rectangle":
                    reader = csv.DictReader(f, fieldnames=['id', 'width',
                                                           'height', 'x', 'y'])
                elif str(cls.__name__) == "Square":
                    reader = csv.DictReader(f, fieldnames=['id', 'size',
                                                           'x', 'y'])
                for row in reader:
                    row = {x: int(y) for x, y in row.items()}
                    temp = cls.create(**row)
                    res.append(temp)
                return res

