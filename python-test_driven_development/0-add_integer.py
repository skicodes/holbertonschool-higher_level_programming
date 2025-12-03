#!/usr/bin/python3
"""
This module contains a function for adding two integers.
It ensures type validation and casts floats to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after validating and converting them to integers if needed.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b after conversion to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
