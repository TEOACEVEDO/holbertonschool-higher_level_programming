#!/usr/bin/python3
"""Models Base
Unittest: tests/test_base.py"""

from os import path
import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """is used for count the number of objects"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Will convert JSON string into a dictionary"""
        if list_dictionaries is None or list_dictionaries == "":
            list_dictionaries = "[]"
            return list_dictionaries
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ JSON string to file"""

        filename = cls.__name__ + ".json"
        if list_objs is not None:
            list_objs = [i.to_dictionary() for i in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns a json strings"""
        str_list = []
        if json_string is None or json_string == "":
            return str_list
        str_list = json.loads(json_string)
        return str_list

    @classmethod
    def create(cls, **dictionary):
        """create a dummy instance"""
        if cls.__name__ == "Rectangle":
            instance = cls(6, 2)

        if cls.__name__ == "Square":
            instance = cls(4)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """a class method that returns a list of instances"""
        if path.exists(cls.__name__ + ".json") is False:
            return []
        listv = []
        with open(cls.__name__ + ".json", "r", encoding='utf-8') as f:
            listv = cls.from_json_string(f.read())
        listv2 = []
        for i in listv:
            if type(i) is dict:
                listv2.append(cls.create(**i))
            else:
                listv2.append(i)
        return listv2
