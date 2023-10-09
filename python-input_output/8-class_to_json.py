#!/usr/bin/python3
"""input and output module"""
import json


def class_to_json(obj):
    """Create a dictionary to hold the serialized data"""
    serialized_data = {}
    for attr_name in dir(obj):
        if attr_name.startswith("_"):
            continue
        attr_value = getattr(obj, attr_name)
        if isinstance(attr_value, (list, dict, str, int, bool)):
            serialized_data[attr_name] = attr_value
    return serialized_data
