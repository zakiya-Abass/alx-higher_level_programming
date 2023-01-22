#!/usr/bin/python3
"""
Module 0-add_integer
Adds two Integers/Floats and
returns the sum
"""


def add_integer(a, b=98):
    """ adds a and b
    Args:
        a (int)
        b (int, optional): Default to 98.
    Raises:
        TypeError: a and b must be an integer
    Returns:
        int: sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + 
