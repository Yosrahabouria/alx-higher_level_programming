#!/usr/bin/python3
"""definition of the class Base"""

from json import dumps, loads
import csv


class Base:
    """Base of classes"""

    __num_objects = 0

    def __init__(self, id=None):
        """Initialization"""

        if id is not None:
            self.id = id
        else:
            type(self).__num_objects += 1
            self.id = type(self).__num_objects

    @staticmethod
    def to_json_string(list_dicts):
        """json string of list_dicts"""

        if list_dicts is None or len(list_dicts) == 0:
            return "[]"
        else:
            return json.dumps(list_dicts)

    @classmethod
    def save_to_file(cls, list_objects):
        """json string of list_objects"""
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
                        writer.writerow([obj.id, obj.width, obj.height,
                                         obj.pos_x, obj.pos_y])
                    elif str(cls.__name__) == "Square":
                        writer.writerow([obj.id, obj.size, obj.pos_x, obj.pos_y])

    @classmethod
    def load_from_file_csv(cls):
        """List of class instances"""
        filename = str(cls.__name__) + ".csv"
        res = []
        if os.path.isfile(filename):
            with open(filename, encoding="UTF-8") as f:

                if str(cls.__name__) == "Rectangle":
                    reader = csv.DictReader(f, fieldnames=['id', 'width',
                                                           'height', 'pos_x', 'pos_y'])
                elif str(cls.__name__) == "Square":
                    reader = csv.DictReader(f, fieldnames=['id', 'size',
                                                           'pos_x', 'pos_y'])
                for row in reader:
                    row = {col: int(val) for col, val in row.items()}
                    temp = cls.create(**row)
                    res.append(temp)
                return res
