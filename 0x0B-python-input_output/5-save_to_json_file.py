#!/usr/bin/python3
"""module: 5-save-to_json_file"""

import json


def save_to_json_file(my_obj, filename):
    """this function is used for write an object to a text file"""
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
