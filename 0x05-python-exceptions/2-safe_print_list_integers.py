#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Function prints the first x elements of a list & only integers

    Args:
        my_list (list): List of any type
        x (int): number of elements to print from list

    Returns: Real number of integers printed
    """
    printed = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return printed
