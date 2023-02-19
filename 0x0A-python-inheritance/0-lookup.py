#!/usr/bin/python3
""" 0-lookup Module
Gets a list of available attributes and methods
of an object
"""


def lookup(obj):
    """ Returns the list of available attributes and methods
    of an object
    Args:
        obj: An instance of a class
    Returns:
        A list of availabe methids and attribute
    """

    return (dir(obj))
