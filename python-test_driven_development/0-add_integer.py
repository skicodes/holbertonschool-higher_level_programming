#!/usr/bin/python3
"""
This module provides a function that adds two numbers safely.
It validates that both inputs are integers or floats and ensures
that they contain finite numeric values (no NaN or infinity).
Floats are cast to integers before the addition. The function
returns an integer result representing the sum of both values.
"""

def add_integer(a, b=98):
    """
    Add two integers after validating and casting inputs.

    This function checks that both arguments are integers or floats,
    ensures they are finite numeric values, casts floats to integers,
    and returns their sum.
    """
    # Validate types
    for value, name in ((a, "a"), (b, "b")):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be an integer")

        # Reject NaN or infinite floats (to avoid ValueError on int())
        if isinstance(value, float):
            if value != value or value in (float("inf"), float("-inf")):
                raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)

