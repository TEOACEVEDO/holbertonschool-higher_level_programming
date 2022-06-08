#!/usr/bin/python3
"""module: 6-load-from_json_file"""


import json


def load_from_json_file(filename):
    """this function is used for read and json.load for created an object"""

    with open(filename, 'r', encoding="utf-8") as f:
         return json.load(f)
