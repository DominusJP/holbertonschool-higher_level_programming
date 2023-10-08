#!/usr/bin/python3
"""input and output module"""
import json


def load_from_json_file(filename):
    """more jason"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
