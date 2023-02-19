#!/usr/bin/python3
""" Base module
Houses a Base class with private attributes
"""
import json
import csv
import os.path


class Base:
    """ Defines the class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes an instance of class
        Args:
            id: (int) Defauls as None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of
        list_dictinaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs
        to a file
        Args:
            list_objs: a list of class instances
        """

        filename = '{}.json'.format(cls.__name__)
        #  print(filename)
        list_dict = []  # a list of object dictionaries
        if list_objs is None or len(list_objs) == 0:
            with open(filename, mode='w') as f:
                f.write("[]")
        else:
            for i, obj in enumerate(list_objs):
                #  print(i)
                list_dict.append(obj.to_dictionary())
            json_string = cls.to_json_string(list_dict)
            with open(filename, mode='w') as f:
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of JSON string representation from json_string
        """

        if json_string is None or len(json_string) == 0:
            return []
        else:

            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attribute set
        Args:
            **dictionary: used as a keyword argument **kwargs
        Return:
            The instance created
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)  # (width, height, x, y, id)
        elif cls.__name__ == 'Square':
            dummy = cls(1)  # (size, x, y, id)
        dummy.update(**dictionary)
        return dummy  # The instance that has all attributes set

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
        """

        filename = '{}.json'.format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        list_instance = []
        with open(filename, 'r') as f:
            json_string = f.read()
        list_dict = cls.from_json_string(json_string)

        for i in range(len(list_dict)):
            list_instance.append(cls.create(**list_dict[i]))

        return list_instance

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Saves a dictionary representation of an instance
        to a CSV file - Serializing
        """

        filename = '{}.csv'.format(cls.__name__)
        if filename == 'Square.csv':
            fields = ['id', 'size', 'x', 'y']
        elif filename == 'Rectangle.csv':
            fields = ['id', 'width', 'height', 'x', 'y']

        l_dict = []
        for obj in list_objs:
            l_dict.append(obj.to_dictionary())

        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(l_dict)
            """
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())
            """

    @classmethod
    def load_from_file_csv(cls):
        """ Returns a list of dictionary from a CSV file
        - Deserializing
        """

        filename = '{}.csv'.format(cls.__name__)
        if os.path.exists(filename) is False:
            return []
        if filename == 'Rectangle.csv':
            fields = ['id', 'width', 'height', 'x', 'y']
        elif filename == 'Square.csv':
            fields = ['id', 'size', 'x', 'y']

        with open(filename) as csvfile:
            csvreader = csv.reader(csvfile)
            objs = []
            for x, row in enumerate(csvreader):
                if x == 0:  # i.e this is the first row or header
                    continue
                obj_dict = {}
                for i, field in enumerate(fields):
                    # print('From csvreader: {}' .format(int(row[i])))
                    obj_dict[field] = int(row[i])

                objs.append(cls.create(**obj_dict))
        return objs
