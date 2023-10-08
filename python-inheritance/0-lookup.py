#!/usr/bin/python3
"""
Python inheritance module
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: A list of attributes and methods.
    """
    return dir(obj)
