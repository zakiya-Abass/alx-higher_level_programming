#!/usr/bin/python3
""" 100-appned_after Module
Defines a functio append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file after each line
    containing a specific string
    Args:
        filename: File to append after
        search_string: string to find in filename
        new_string: string to replace search string with
    """

    text = ""
    with open(filename) as f:
        for line in f:
            s = s + line
            if search_string in line:
                s = s + new_string
    with open(filename, 'w') as f_w:
        f_w.write(s)
