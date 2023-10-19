#!/usr/bin/python3
from sys import argv

if __name__ == "__main":
    # Get the number of arguments
    num_args = len(argv) - 1

    # Print the number of arguments and whether they are singular or plural
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Print the arguments with their positions
    for i in range(1, num_args + 1):
        print(f"{i}: {argv[i]}")
        