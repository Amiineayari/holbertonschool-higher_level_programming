#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Get the number of command-line arguments
    i = len(sys.argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    # If there is at least one argument, iterate through the arguments
    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                # Print the index and value of each argument
                print("{}: {}".format(i, arg))
            i += 1
            