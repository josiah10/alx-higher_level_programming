#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)

    new_list = my_list[:]

    if 0 <= idx < length:
        new_list[idx] = element

    return (new_list)
