#!/usr/bin/python3
"""No module imported"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes a square
        Args:
            size: length of each side
            position: coordinate to locate square
        """
        self.size = size
        self.position = position

    def area(self):
        """Computes the area of the square
        Returns: the result
        """
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        i, j = value
        if isinstance(i, int) and isinstance(j, int):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        if i < 0 or j < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(pow(self.__size, 2)):
                if (i % self.__size == 0):
                    if i != 0:
                        print()
                    for i in range(self.__position[0]):
                        print(' ', end='')
                print('#', end='')
            print()
