#!/usr/bin/python3
"""this function is used to know if the obj"""
"""is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """it checks if the obj is of the class"""
    if type(obj) is a_class:
        return True
    else:
        return False
