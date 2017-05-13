#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Write a function that divides element by element 2 lists.
    my_list_1 and my_list_2 can contain any type (integer, string, etc.)
    list_length can be bigger than the length of both lists
    
    Handle following exceptions:
    If 2 elements can't be divided, the division result should be equal to 0
    If an element is not an integer or float:
    print: wrong type
    If the division can't be done (/0):
    print: division by 0
    If my_list_1 or my_list_2 is too short
    print: out of range
    Returns a new list (length = list_length) with all divisions
    
    You have to use try: / except: / finally:
    You are not allowed to import any module
    """
    result = []
    for i in range(list_length):
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
            div = 0
    return (result)
