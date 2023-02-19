#!/usr/bin/python3
""" 6-load_from_json_file Module
Defines a function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ Creates an Onject from a "JSON" file
    Args:
        filename: JSON file
    """

    with open(filename) as f:
        return json.load(f)
