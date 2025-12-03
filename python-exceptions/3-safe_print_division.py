#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints the result in a debug message.

    Args:
        a (int): Dividend
        b (int): Divisor

    Returns:
        float: Result of division if successful, otherwise None
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
