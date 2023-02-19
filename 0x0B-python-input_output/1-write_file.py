#!/usr/bin/python3
""" 1-write_file Module
Defines a function write_file
"""


def write_file(filename="", text=""):
    """ Writes a strimg to a text file (UTF8)
    Args:
        filename: File to write text into
        text: string to be added to filename
    Returns: Number of chaacter written
    """

    with open(filename, mode='w', encoding="utf-8") as t_file:
        return t_file.write(text)
