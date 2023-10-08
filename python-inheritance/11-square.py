#!/usr/bin/python3
"""last rectangle exersice"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area of the rectangle"""
        return self.__size ** 2
