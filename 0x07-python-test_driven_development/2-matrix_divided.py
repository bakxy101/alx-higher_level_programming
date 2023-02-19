#!/usr/bin/python3

def matrix_divided(matrix, div):
    zero_division = "division by zero"
    number_div = "div must be a number"
    same_size = "Each row of the matrix must have the same size"
    list_of_list = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(list_of_list)
    elif len(matrix) == 0:
        raise TypeError(list_of_list)
    else:
        for elem in matrix:
            if type(elem) is not list:
                raise TypeError(list_of_list)

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError(same_size)
        elif len(row) == 0:
            raise TypeError(list_of_list)
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(list_of_list)

    if type(div) not in [int, float]:
        raise TypeError(number_div)
    elif div == 0:
        raise ZeroDivisionError(zero_division)

    return [[round(elem / div, 2) for elem in row] for row in matrix]
