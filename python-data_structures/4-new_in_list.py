#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list.copy()  # Return a copy of the original list if idx is out of range or negative
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
