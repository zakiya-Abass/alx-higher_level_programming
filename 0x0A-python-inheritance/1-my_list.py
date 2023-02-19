#!/usr/bin/python3
""" 1-my_list Module
Contains a derived class or a subClass
"""


class MyList(list):
    """
    A subclass MyList of list
    """

    def print_sorted(self):
        """ Prints list in a sorted order(ascending) """

        new_sort_list = self[:]
        new_sort_list.sort()
        print("{}".format(new_sort_list))
