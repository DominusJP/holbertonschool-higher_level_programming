#!/usr/bin/python3
"""input output"""


class Student:
    """Write a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the object to a JSON-like dictionary"""
        if attrs is None:
            attrs = [attr for attr in dir(self) if not attr.startswith("_")]
        serialized_data = {}
        for attr_name in attrs:
            attr_value = getattr(self, attr_name, None)
            if self.is_serializable(attr_value):
                serialized_data[attr_name] = attr_value
        return serialized_data

    def reload_from_json(self, json):
        """Reload object attributes from a dictionary"""
        for attr_name, attr_value in json.items():
            setattr(self, attr_name, attr_value)

    @staticmethod
    def is_serializable(value):
        """Check if a value is serializable (str or int)"""
        return isinstance(value, (str, int))
