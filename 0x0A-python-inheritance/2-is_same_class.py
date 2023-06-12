#!/usr/bin/python3
"""returns True if the object is exactly an instance of the specified class
; otherwise False.
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance"""
    return True if type(obj) == a_class else False
