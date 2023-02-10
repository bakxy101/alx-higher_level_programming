#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq = set()
    for elem in my_list:
        if elem not in uniq:
            uniq.add(elem)
    return sum(uniq)
