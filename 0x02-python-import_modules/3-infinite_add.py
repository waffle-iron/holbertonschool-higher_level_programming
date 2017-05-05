#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv)
    for i in range (1, count):
        i = int(sys.argv[i]) + i
    print(i)
