#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ function divides all elements of a matrix."""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(" matrix must be a matrix" +
                        "(list of lists) of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError(" matrix must be a matrix" +
                            "(list of lists) of integers/floats")
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in r:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)" +
                                "of integers/floats")
        return ([[round(i /div, 2) for i in r] for r in matrix])
