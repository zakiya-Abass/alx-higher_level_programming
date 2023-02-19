#!/usr/bin/python3
"""4-inherits_from Module
Contains a function that returns true or false
if an object is an instance of a class directly or indirectly
"""


def inherits_from(obj, a_class):
    """ Returns True if an object is an instance of a class
    or an inherited class
    Args:
        obj: (an instance)
        a_class: (a class)
    Return:
        True or False
    """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
