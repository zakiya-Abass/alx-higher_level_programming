#!/usr/bin/python3
""" Defines a function: text_indentation """


def text_indentation(text):
    """ prints a text with 2 new lines after each of
    these characters: '.', '?' and ':'
    Args:
        text (str): string to be printed
    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        print(text[i], end='')
        if text[i] in ['.', '?', ':']:
            print('\n')
            j = i + 1
            while text[j] == ' ':
                i += 1
                j += 1
        i += 1
