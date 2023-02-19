#!/usr/bin/python3
""" 2-is_same_class Module
Checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """ Returns True if an object is an instance
    of a class
    Args:
        obj: (an instance)
        a_class: (a class)
    Return:
        True - if obj is an instance of a_class
        False - Otherwise
    """

    if type(obj) is a_class:
        return True
    else:
        return False
