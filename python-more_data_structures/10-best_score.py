#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    best_value = None
    for key, value in a_dictionary.items():
        if isinstance(value, int) and (best_value is None or value > best_value):
            best_value = value
            best_key = key
    return best_key
