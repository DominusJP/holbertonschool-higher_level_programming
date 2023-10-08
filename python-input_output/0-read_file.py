#!/usr/bin/python3
"""input and output module"""


def read_file(filename=""):
    """function to print something from a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
