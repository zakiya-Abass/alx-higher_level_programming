#!/usr/bin/python3
""" 100-my_int Module
mimics class <int> as a rebel
"""


class MyInt(int):
    """ Defines a subclass MyInt of int """

    def __ne__(self, other):
        """ Defines the != comparison """

        return super().__eq__(other)

    def __eq__(self, other):
        """ Defines the equality comparison """

        return super().__ne__(other)
