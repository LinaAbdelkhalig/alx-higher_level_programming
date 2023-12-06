#!/usr/bin/python3
def square(x):
    return x * x
def square_matrix_simple(matrix=[]):
    matrix_cp = list(map(lambda row: list(map(square, row)),matrix))
    return matrix_cp
