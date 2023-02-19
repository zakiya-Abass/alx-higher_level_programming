#!/usr/bin/python3
""" 0-read_file Module
Defines a function read_file
"""


def read_file(filename=""):
    """ Reads a test file with UTF8 encoding
    and prints to stdout
    Args:
        filename: Text file to read (defaults to '')
    """

    with open(filename, encoding='utf-8') as t_file:
        file_read = t_file.read()
        for f in file_read:
            print("{}".format(f), end='')
