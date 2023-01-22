#!/usr/bin/python3
""" Defines a function: say_my_name"""


def say_my_name(first_name, last_name=""):
    """ prints a person's full name
    Args:
        first_name (str): The person's first name
        last_name (str): The person's last name
    Raises:
        TypeError: If either of first_name or last_name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
