#!/usr/bin/python3
""" square Module
Houses a subclass Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the subclass Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints an informal representation of an instance
        """

        id = self.id
        x = self.x
        y = self.y
        width = self.width
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, width))

    @property
    def size(self):
        """ Retrieves the size of square
        """

        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size of square to value
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns attributes to an instance
        """

        list_t = ['id', 'size', 'x', 'y']
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                setattr(self, list_t[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square
        """

        new_dict = {}
        list_t = ['id', 'size', 'x', 'y']
        for key in list_t:
            new_dict[key] = getattr(self, key)
        return new_dict
