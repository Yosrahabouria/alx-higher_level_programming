#!/usr/bin/python3
"""
Contains definition of the class Base
"""
import json
import csv


class Base:
    """base of classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation"""

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json string of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objects):
        """Writing JSON string  of list_objects to file"""
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
    def from_json_string(json_string):
        """list representation of a JSON string"""
        if json_string is None or len(json_string) == 0:
            res = []
            return res
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class instance with all attributes"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Square":
            temp = Square(1)
        elif cls.__name__ == "Rectangle":
            temp = Rectangle(2, 7)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """list of class instances"""
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
        """csv of python list_objects"""
        if list_objects is None:
            filename = str(type(self).__name__) + ".json"
            with open(filename, mode="w", encoding="UTF-8") as f:
                f.write("[]")
        else:
            filename = str(type(list_objects[0]).__name__) + ".csv"
            with open(filename, mode="w", encoding="UTF-8") as f:
                writer = csv.writer(f)
                for obj in list_objects:
                    if str(cls.__name__) == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
                    elif str(cls.__name__) == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """list of class instances"""
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
