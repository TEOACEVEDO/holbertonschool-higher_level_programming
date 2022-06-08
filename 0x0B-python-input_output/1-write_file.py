#!/usr/bin/python3
"""module: 1-write-file"""


def write_file(filename="", text=""):
    """this function is used for write file"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
