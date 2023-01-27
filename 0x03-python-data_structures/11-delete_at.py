#!/usr/bin/python3

def delete_at(my_list: list = [], idx: int = 0) -> list:
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
        return my_list
    return my_list
