#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    max_score = 0
    key = None
    for k, v in my_dict.items():
        if v > max_score:
            max_score = v
            key = k
    return key
