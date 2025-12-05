#!/usr/bin/python3
"""
This module provides a function for safely adding two integers.
It validates inputs, handles special float values, and returns an integer.
"""


def add_integer(a, b=98):
    """
    Add two integers, validating and converting float inputs when needed.

    Returns the integer sum of a and b.
    """
    # Validate a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Reject NaN
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")

    # Reject +/- infinity
    if a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")

    # Validate b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")

    if b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
