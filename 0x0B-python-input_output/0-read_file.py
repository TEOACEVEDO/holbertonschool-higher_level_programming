#!/usr/bin/python3
"""module: 0-read_file"""


def read_file(filename=""):
    """this function is used for open file"""

    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
