#!/usr/bin/python3
"""
This module provides a function for adding two integer values safely.
It ensures that inputs are of valid types before performing the operation.
The function supports both integers and floats as arguments.
All float values are first cast to integers before addition.
"""


def add_integer(a, b=98):
    """
    Add two integers after validating their types and casting floats.

    Returns the integer result of a + b.
    """

    # Validate a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    # Detect NaN
    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")
    # Detect +inf / -inf
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
