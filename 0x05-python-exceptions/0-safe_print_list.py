#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for item in my_list:
        try:
            if count < x:
                print("{}".format(item), end="")
                count += 1
        except (IndexError, TypeError):
            pass
    print("")
    return(count)
