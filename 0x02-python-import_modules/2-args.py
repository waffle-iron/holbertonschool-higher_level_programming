#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for i in sys.argv[1:]:
        if len(sys.argv) > 1:
            print("{:d}\n {}".format(len(sys.argv), sys.argv[1:]))
