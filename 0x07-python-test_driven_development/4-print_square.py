#!/usr/bin/python3
""" Defines a function: print_square"""


def print_square(size):
    """ prints a square with the '#' character
    Args:
        size (int): size of the square
    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
        TypeError: if size is a float and less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and (size < 0):
        raise TypeError("size must be an integer")

    for i in range(pow(size, 2)):
        if not (i % size) and (i != 0):
            print()
        print(f"#", end='')
    if size != 0:
        print()
