#!/usr/bin/python3
"""module: 4-from-json_string"""

import json


def from_json_string(my_str):
    """this function is used for returns represented by a JSON string"""

    return json.loads(my_str)
