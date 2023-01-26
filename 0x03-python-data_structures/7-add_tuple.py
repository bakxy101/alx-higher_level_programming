#!/usr/bin/python3

def add_tuple(tuple_a: tuple = (), tuple_b: tuple = ()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if len(list_a) >= len(list_b):
        for idx in range(len(list_b)):
            list_a[idx] += list_b[idx]
        if (len(list_a) == 1):
            return (list_a[0], 0)
        elif len(list_a) == 0:
            return (0, 0)
        return (list_a[0], list_a[1])
    elif len(list_b) > len(list_a):
        for idx in range(len(list_a)):
            list_b[idx] += list_a[idx]
        if (len(list_b) == 1):
            return (list_b[0], 0)
        elif len(list_b) == 0:
            return (0, 0)
        return (list_b[0], list_b[1])
