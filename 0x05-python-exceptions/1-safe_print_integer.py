#!/usr/bin/python3
def safe_print_integer(value):
    for item in my_list:
        try:
            print("{:d}".format(value))
        except (IndexError, TypeError, ValueError):
            return(False)
        except:
            return(True)
