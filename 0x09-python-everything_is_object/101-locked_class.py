#!/usr/bin/python3
"""prevent the user from dynamically creating new instance attributes"""


class LockedClass(object):
    """__slots__prevent the user from dynamically creating new instance"""

    __slots__ = 'first_name'

    def __init__(self, first_name=""):
        """instantiation with optional first_name"""
        self.first_name = first_name
