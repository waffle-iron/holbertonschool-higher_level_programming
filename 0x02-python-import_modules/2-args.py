#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    for i in sys.argv[1:]:
        if count > 1:
            print("{:d}\n {}".format(count, sys.argv[1:]))
