#!/usr/bin/python3
"""more about this project, input output"""


def class_to_json(obj):
    """comentando la clase"""
    serialized_data = {}
    for attr_name in dir(obj):
        # Skip private attributes and methods (those starting with an underscore)
        if attr_name.startswith("_"):
            continue
        
        # Get the attribute value
        attr_value = getattr(obj, attr_name)
        
        # Check if the attribute value is serializable
        if is_serializable(attr_value):
            serialized_data[attr_name] = attr_value

    return serialized_data

def is_serializable(value):
    """Check if a value is serializable
    (list, dict, str, int, or bool)"""
    return isinstance(value, (list, dict, str, int, bool))
