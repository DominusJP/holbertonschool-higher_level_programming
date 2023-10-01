#!/usr/bin/python3
"""Module 4, test driven development."""


def add_integer(a, b=98):
    """
    adding two integers
    """
    if (isinstance(a, int) or isinstance(a, float)):
        if (isinstance(b, int) or isinstance(b, float)):
            a = int(a)
            b = int(b)
            return a + b
    else:
        raise TypeError("a must be an integer or b must be an integer")
