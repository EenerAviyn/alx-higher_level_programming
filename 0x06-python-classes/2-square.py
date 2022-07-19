#!/usr/bin/python3
"""Square module - assigns size, checks type, value"""


class Square:
    """Defines square with private instance attribute size"""

    def __init__(self, size=0):
        """assigns size of square and checks type and value"""

        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        if size < 0:
            raise ValueError("size mmust be >= 0")
        self.__size = size
