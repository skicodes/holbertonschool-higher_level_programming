#!/usr/bin/python3
"""
This module provides a function that performs the addition of two numbers.
It ensures that the inputs are either integers or floats and raises an error
otherwise. The function casts floats to integers before performing addition.
It returns the computed integer result of adding the two provided values.
"""


def add_integer(a, b=98):
    """
    Add two integers after validating and casting inputs.

    This function checks that both arguments are integers or floats,
    casts floats to integers, and returns their sum.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
