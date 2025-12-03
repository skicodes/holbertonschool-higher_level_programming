#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer safely using '{:d}'.format().
    
    Args:
        value: Any type, expected to be an integer.
    
    Returns:
        True if value is an integer and was printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
