#!/usr/bin/python3
"""Square module"""


class Square:
    """defines square with private instance attribute size"""
    def __init__(self, size=0):
        """Constructor.
        Args:
            size: Length of side of square
        """
        self.size = size

    @property
    def size(self):
        """Retrieves value of size
        Raises:
            TypeError: If size is not int
            ValueError; If size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter - sets value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public instance method returns current sqr area"""

        return self.__size ** 2

    def my_print(self):
        """prints square to stdout with char #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
