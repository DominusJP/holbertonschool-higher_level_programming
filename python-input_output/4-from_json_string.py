#!/usr/bin/python3
"""input and output module"""
import json


def from_json_string(my_str):
    """doing the oposite"""
    return json.loads(my_str)
