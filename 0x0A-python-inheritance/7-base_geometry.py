#!/usr/bin/python3
""" 6-base-geometry Module
Houses a class BaseGeometry that
raises an Exception and validates a value
"""


class BaseGeometry:
    """ Defines the class BaseGeometry"""

    def area(self):
        """ Raises an Exception """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validates value
        Args:
            name
            value
        Raises: TypeError: <name> must be an integer
                ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
