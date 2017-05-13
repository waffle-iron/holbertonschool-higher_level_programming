#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except (TypeError):
            print("{:s}".format("wrong type"))
        except (ZeroDivisionError):
            print("{:s}".format("division by 0"))
        except (IndexError):
            print("{:s}".format("out of range"))
        finally:
            result.append(div)
    return (result)
