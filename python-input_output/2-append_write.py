#!/usr/bin/python3
"""input and output module"""


def append_write(filename="", text=""):
    """appending a string"""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            num_chars_added = file.write(text)
        return num_chars_added
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0  # Return 0 if an error occurs
