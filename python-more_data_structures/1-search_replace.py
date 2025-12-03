#!/usr/bin/python3
"""
Function that replaces all occurrences of an element by another
in a new list.
"""


def search_replace(my_list, search, replace):
    """
    Returns a new list with all occurrences of `search` replaced by `replace`.
    """
    return [replace if x == search else x for x in my_list]
