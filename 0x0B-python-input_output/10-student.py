#!/usr/bin/python3
""" 10-student Module
Houses a class Student
"""


class Student:
    """ Defines the class Student """

    def __init__(self, first_name, last_name, age):
        """ Initializes an instance of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of
        a Student instance
        """

        if type(attrs) is list:
            for word in attrs:
                if type(word) is not str:
                    return self.__dict__

            new_dict = {}

            # Moving through he list in attrs
            for element in range(len(attrs)):
                for key in self.__dict__:
                    # if any elemnet in list attrs is the same as a key
                    # in self.__dict__
                    if attrs[element] == key:
                        # copy that element into a new dict
                        new_dict[key] = self.__dict__[key]
            return new_dict

        return self.__dict__
