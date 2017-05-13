#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    best_score = 0
    key = 0
    for k, v in my_dict.items():
        if v > best_score:
            best_score = v
            key = k
    return key
