#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """Class rectangle that defines a rectangel by based on 0-rectangle.py"""

    def __init__(self, width=0, height=0):
        """ Constructor Method for Rectangle """

        self.__height = height
        self.__width = width

    @property
    def height(self, value):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not type(value) is (int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

    @property
    def width(self):
        """Private instnace attributte: width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not type(value) is (int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

    def area(self):
        return self.width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """Returns string representation of a Rectangle"""

        if self.width == 0 or self.__height == 0:
            return ""
        new_string = ""
        for i in range(self.__height):
            new_string += "#" * self.__width
            if i < self.__height - 1:
                new_string += "\n"
        return new_string

    def __repr__(self):
        """Returns a String with a representation of the state of the object"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete an instance"""
        print('Bye rectangle...')
