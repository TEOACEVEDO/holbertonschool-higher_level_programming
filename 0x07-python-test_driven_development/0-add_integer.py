#!/usr/bin/python3
"""
Add two integer
"""


def add_integer(a, b=98):
    """
    Returns:
        The addition of the two given numbers
    """
    if not type(a) is (int, float):
        raise TypeError('a must be an integer')

    if not type(b) is (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
