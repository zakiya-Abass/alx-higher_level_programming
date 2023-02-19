#!/usr/bin/python3
""" 8-class_to_json Module
Defines a fnction class_to_json
"""


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure
    for JSON serialization of an object
    Args:
        obj: an instance of class
    """
    return obj.__dict__
