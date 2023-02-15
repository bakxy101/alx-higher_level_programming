#!/usr/bin/python3


def safe_print_list(my_list: list =[], x=0) -> int:
    """Prints elements of a list and returns actual printed count

    Args:
        my_list (list): List of elements
        x (int): Number of elements to print

    Returns:
        Number of actual printed elements from the list
    """
    for idx in range(x):
        try:
            print(my_list[idx], end="")
        except:
            print()
            return (idx)
    print()
    return (x)
