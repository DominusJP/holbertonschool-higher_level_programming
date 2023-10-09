#!/usr/bin/python3
"""input and output module"""
import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
# Check if any command-line arguments are provided
if len(sys.argv) > 1:
    # Try to load the existing JSON data from the file
    try:
        existing_data = load_from_json_file("add_item.json")
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    # Add the command-line arguments to the existing data
    existing_data.extend(sys.argv[1:])

    # Save the updated data to the file
    save_to_json_file(existing_data, "add_item.json")
    print("Arguments added and saved to 'add_item.json'.")
else:
    print("No arguments provided. Nothing to add.")
