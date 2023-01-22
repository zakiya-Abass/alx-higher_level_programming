#!/usr/bin/python3
"""Defines a class 'Square'"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): size of new square
        """

        self.size = size

    def area(self):
        """Returns the area of instance of square"""
        return (pow(self.__size, 2))

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the current size of the square."""
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

