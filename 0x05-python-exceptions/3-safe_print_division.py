#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("{:s}".format("Inside result: None"), end="")
    finally:
        print("{:s}".format("Inside result: "), end="")
