#!/usr/bin/python3
""" 2-append_write Module
Defines a function append_write
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file(UTF8)
    Args:
        filename: File to append into (Defaults to '')
        text: string to append to filename
    Returns: Number of characters added
    """

    with open(filename, mode='a', encoding="utf-8") as t_file:
        return t_file.write(text)
