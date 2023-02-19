#!/usr/bin/python3
""" 5-save_to_json_file Module
Defines a function save_to_json
"""
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file (UFT8) using a JSON representation
    Args:
        my_obj: A python object
        filename: text file to write json of my_obj to
    """

    with open(filename, mode='w', encoding='utf-8') as t_file:
        t_file.write(json.dumps(my_obj))
