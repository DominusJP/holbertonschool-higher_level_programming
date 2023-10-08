#!/usr/bin/python3
"""
Python inheritance module
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending order.

        """
        if all(isinstance(i, int) for i in self):
            print(sorted(self))
