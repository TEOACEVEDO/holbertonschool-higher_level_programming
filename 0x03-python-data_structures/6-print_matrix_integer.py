#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # verificar que si exista la matrix
    if matrix:
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                print(matrix[y][x], end="")
                if x < len(matrix[y]) - 1:
                    print(" ", end='')
            print()
