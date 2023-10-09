#!/usr/bin/python3
"""more about this project, input output"""


def class_to_json(obj):
    """comentando la clase"""
    serialized_data = {}
    for attr_name in dir(obj):
        if attr_name.startswith("_"):
            continue
        attr_value = getattr(obj, attr_name)
        if is_serializable(attr_value):
            serialized_data[attr_name] = attr_value
    return serialized_data


def is_serializable(value):
    """Check if a value is serializable
    (list, dict, str, int, or bool)"""
    return isinstance(value, (list, dict, str, int, bool))
