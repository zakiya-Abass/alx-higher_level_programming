#!/usr/bin/python3
""" rectangle Module
Houses a subclass Rectangle
"""
from models.base import Base
import json

Class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Sets (y) as a private attribute """
        super().__init_(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Sets (y) as a private attribute """
        return self.__width

    @width.setter
    def width(self,values):
        """Sets (y) as a private attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif type(value) <= 0:
            raise TypeError("width must be greater than 0")
        else:
            return self.__width

    @property
    def height(self):
        """Sets (y) as a private attribute """
        return self.__height

    @height.setters
    def height(self, values):
        """Sets (y) as a private attribute """
        if type(values) is not int:
            raise TypeError("height must be an integer")
        elif type(values) <= 0:
            raise TypeError("height must be greater than 0")
        else:
            return self.__height

    @property
    def x(self):
        """Sets (y) as a private attribute """
        return self.__x

    @height.setters
    def x(self, values):
        """Sets (y) as a private attribute """
        if type(values) is not int:
            raise TypeError("x must be an integer")
        elif type(values) <= 0:
            raise TypeError("x must be greater than 0")
        else:
            return self.__x

    @property
    def y(self):
        """Sets (y) as a private attribute """
        return self.__y

    @height.setters
    def y(self, values):
        """Sets (y) as a private attribute """
        if type(values) is not int:
            raise TypeError("y must be an integer")
        elif type(values) <= 0:
            raise TypeError("y must be greater than 0")
        else:
            return self.__y

    def area(self):
        """Sets (y) as a private attribute """
        return  self.__width * self.__height

    def display(self):
        """Sets (y) as a private attribute """
        print("\n" * self.__y, end='')
        for y in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)
