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


class Rectangle(BaseGeometry):
    """ Defines a subclass Rectangle of BaseGeometry """

    def __init__(self, width, height):
        """ Initializes an instance of a Rectangle
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """ Prints and informal represtation of an instance of self """

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """ Gets the area od a Rectangle
        Doesn't cause a class with the area method in the supper class
        """

        return (self.__width * self.__height)


class Square(Rectangle):
    """ Defines a subclass Square of Rectangle """

    def __init__(self, size):
        """ Initializes an instance of a Square """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """ Prints an informal represtation of an instance of self """
        return super().__str__()

    def area(self):
        """ Returns the area of an instance Square"""

        return self.__size ** 2
