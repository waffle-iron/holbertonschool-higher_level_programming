#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for number in my_list:
        if number == search:
            number = replace
        else:
            number
    return(my_list)

return [replace if item == search else item for item in my_list]
