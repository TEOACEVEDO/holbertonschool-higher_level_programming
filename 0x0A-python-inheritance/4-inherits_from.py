#!/usr/bin/python3
"""module: 2-is_same_class"""


def inherits_from(obj, a_class):
    """issubclass is used for compare two class"""

    if isinstance(obj, a_class) & issubclass(a_class, obj.__class__) is False:
        return True
    return False
