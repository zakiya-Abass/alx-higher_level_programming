#!/usr/bin/python3
""" 3-is_kind_of_class Module
Checks if an object is an instance of a class
or from an inherit class
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if an object is an instance
    of a class or an inherit class
    Args:
        obj: (an instance)
        a_class: (a class)
    Return:
        True - if obj is an instance of a_class
        False - Otherwise
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
