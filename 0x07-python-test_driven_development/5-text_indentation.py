#!/usr/bin/python3
"""
Print a text with 2 new lines after
each of these characters
. ? :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    """

    if not type(text) is (str):
        raise TypeError("text must be a string")

    for i in text:
        if i in ['.', '?', ':']:
            print(i, end='')
            print()
            print()
        else:
            print(i, end='')
