#!/usr/bin/python3
"""No module imported"""


class Square:
    """Defines a class: Square with a private attribute: size and checks Errors
      and returns the area of the square. Prints in stdout the square with the
      character '#'"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return pow(self.__size, 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(pow(self.__size, 2)):
                if (i % self.__size == 0) and i != 0:
                    print()
                print('#', end='')
            print()
