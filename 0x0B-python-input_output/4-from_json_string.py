#!/usr/bin/python3
""" 4-from_json_string Module
Defines a function from_json_string
"""
import json


def from_json_string(my_str):
    """ Retuns an object(Python data structure) represeneted
    by a JSON string
    Args:
        my_str: A JSON string
    Returns: A Python Object of the JSON string
    """

    return json.loads(my_str)
