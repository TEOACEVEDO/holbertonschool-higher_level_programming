#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = matrix[:].copy()
    for i in range(len(matrix_2)):
        for x in range(len(matrix_2[i])):
            matrix_2[i][x] = (matrix_2[i][x])**2
    return matrix_2
