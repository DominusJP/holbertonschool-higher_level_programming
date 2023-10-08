#!/usr/bin/python3
"""input and output module"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the number of c written"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_chars_written = file.write(text)
        return num_chars_written
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0  # Return 0 if an error occurs
