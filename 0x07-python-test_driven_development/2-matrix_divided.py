#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ function divides all elements of a matrix."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(" matrix must be a matrix" +
                        "(list of lists) of integers/floats")
        l = len(matrix[0])
        for i in matrix[1:]:
            if not isinstance(i, list) or len(i) != l:
                raise TypeError("Each row of the matrix must have the same size")
            for a in i:
                if not isinstance(a, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists)" +
                                    "of integers/floats")
    return ([[round(a /div, 2) for a in i] for i in matrix])
