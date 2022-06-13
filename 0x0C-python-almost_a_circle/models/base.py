#!/usr/bin/python3
"""Models Base"""


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
