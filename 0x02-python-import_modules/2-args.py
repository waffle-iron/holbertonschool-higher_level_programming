#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    if count == 1:
        print("0 argument.")
    if count == 2:
        print ("1 argument:")
    if count > 2:
        print("{:d} arguments:".format(count)
    for i in range(1, count):
       print("{:d}\n {}".format(count, sys.argv[1:]))
