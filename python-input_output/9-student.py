#!/usr/bin/python3
"""more input output excersises"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """getting shit done"""
        serialized_data = {}
        for attr_name in dir(self):
            if attr_name.startswith("_"):
                continue
            attr_value = getattr(self, attr_name)
            if self.is_serializable(attr_value):
                serialized_data[attr_name] = attr_value
        return serialized_data

    @staticmethod
    def is_serializable(value):
        """checking if serializable"""
        return isinstance(value, (str, int))
