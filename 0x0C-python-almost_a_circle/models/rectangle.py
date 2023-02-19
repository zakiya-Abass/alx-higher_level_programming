#!/usr/bin/python3
""" rectangle Module
Houses a subclass Rectangle
"""
from models.base import Base
import json


class Rectangle(Base):
    """ Defines the Rectangle subclass
    """

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieves the private attribute (width)"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the class to value """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Retrives the private attribute (height) """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the (height) as a private attribute """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ Retrieves the private attribute (x) """
        return self.__x

    @x.setter
    def x(self, value):
        """Sets (x) as a private attribute """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ Retrieves the private attribute (y) """
        return self.__y

    @y.setter
    def y(self, value):
        """Sets (y) as a private attribute """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle
        """

        return self.__width * self.__height

    def display(self):
        """ Prints a graphical representation of a Rectangle
        instance to stdout with the character '#'
        """

        print("\n" * self.__y, end='')
        for y in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """ Prints an informal representaion of an instance Rectangle
        """
        id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h))

    def update(self, *args, **kwargs):
        """ Assigns an argument args to each attribute
        """

        list_t = ['id', 'width', 'height', 'x', 'y']
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, list_t[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary representation of a Rectangle
        """

        list_t = ['id', 'width', 'height', 'x', 'y']
        new_dict = {}
        for element in range(len(list_t)):
            for key in list_t:
                new_dict[key] = getattr(self, key)
        return (new_dict)
