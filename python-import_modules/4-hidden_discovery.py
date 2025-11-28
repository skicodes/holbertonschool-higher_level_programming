#!/usr/bin/python3
"""Print names defined in hidden_4.pyc, excluding private names"""

import dis

if __name__ == "__main__":
    # Load the compiled module
    import hidden_4

    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter out names starting with "__"
    public_names = [name for name in names if not name.startswith("__")]

    # Print one per line in alphabetical order
    for name in sorted(public_names):
        print(name)
