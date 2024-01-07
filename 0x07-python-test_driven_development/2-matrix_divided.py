#!/usr/bin/python3
""" Module for the matrix_divide function """


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    Args:
        matrix: list of ints or floats to be divided
        div: number to be divided by

    Return:
        a new matrix

    Raises:
        TypeError: if element of the matrix is not int or float
        TypeError: if rows of matrix are not the same size
        TypeError: if div is not a float or number
        ZeroDivisionError: if div is 0
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
