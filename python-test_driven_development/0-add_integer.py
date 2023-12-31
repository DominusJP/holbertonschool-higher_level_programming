#!/usr/bin/python3
"""Module 4, test driven development."""


def add_integer(a, b=98):
    """
    adding two integers
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
