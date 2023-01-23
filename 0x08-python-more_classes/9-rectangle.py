#!/usr/bin/python3
"""Module to create a class
"""


class Rectangle:
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes a square
        Args:
            size: length of each side
            position: coordinate to locate square
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if not self.__height or not self.__width:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):
        for i in range(self.area()):
            if i and not (i % self.__width):
                print()
            print(self.print_symbol, end='')
        return ''

    def __repr__(self):
        string1 = "Rectangle(" + str(self.__width) + ','
        string2 = str(self.__height) + ')'

        return string1 + ' ' + string2

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        a = Rectangle.area(rect_1)
        b = Rectangle.area(rect_2)

        if a >= b:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance """
        return cls(size, size)
