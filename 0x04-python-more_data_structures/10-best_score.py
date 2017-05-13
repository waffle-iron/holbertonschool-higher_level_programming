#!/usr/bin/python3
def best_score(my_dict):
    """
    Write a function that returns a key with the biggest integer value.
    You can assume that all values are only integers
    If no score found, return None
    You can assume all students have a different score
    You are not allowed to import any module
    """
    if my_dict is None:
        return None
    max_score = 0
    key = 0
    for k, v in my_dict.items():
        if v > max_score:
            max_score = v
            key = k
    return key
