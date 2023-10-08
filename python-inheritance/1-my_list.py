#!/usr/bin/python3
"""
Python inheritance module
"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending order.

        """
        sorted_list = sorted(self)
        print(sorted_list)
