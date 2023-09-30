#!/usr/bin/python3
"""Empezamos con los comentarios/we start with the comments"""


class Square:
    """
    Does this work like this?
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
