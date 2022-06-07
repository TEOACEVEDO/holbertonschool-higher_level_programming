#!/usr/bin/python3
"""A subclass that exist without the need of a parent class"""


class MyList(list):
    """this class return and print a list sorted"""
    def print_sorted(self):
        return print(sorted(self))
