#!/usr/bin/python3
"""Print the number of and list of command-line arguments"""

import sys


if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name
    count = len(args)

    if count == 0:
        print("0 arguments.")
    else:
        word = "argument" if count == 1 else "arguments"
        print("{} {}:".format(count, word))
        for i, arg in enumerate(args, 1):
            print("{}: {}".format(i, arg))
