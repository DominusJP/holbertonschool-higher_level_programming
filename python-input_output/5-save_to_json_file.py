#!/usr/bin/python3
"""input and output module"""
import json


def save_to_json_file(my_obj, filename):
    """json the man"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)
