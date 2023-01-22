#!/usr/bin/python3
"""defining a class 'MagicClass' that does the same as the Bytecode provided"""

import math


class MagicClass:
    """defines a class 'MagicClass'"""

    def __init__(self, radius=0):
        """initialise instance
        Args:
            radius (int or float): The radius of the circle
        """
        if type(radius) != int and type(radius) != float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """finds the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """finds the circumference of the circle"""
        return (2 * math.pi) * self.__radius
