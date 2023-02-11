#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary: dict)-> None:
    for k, v in dict(sorted(a_dictionary.items())).items():
        print(f"{k}: {v}")
