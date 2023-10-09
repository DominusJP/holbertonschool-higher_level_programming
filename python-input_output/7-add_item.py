#!/usr/bin/python3
"""input and output module"""
import json


def save_to_json_file(my_obj, filename):
    """Function to save a Python object to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)


def load_from_json_file(filename):
    """Function to load a Python object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


if len(sys.argv) > 1:
    try:
        existing_data = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    existing_data.extend(sys.argv[1:])
    save_to_json_file(existing_data, "add_item.json")
    print("Arguments added and saved to 'add_item.json'.")
else:
    print("No arguments provided. Nothing to add.")
