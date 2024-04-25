#!/usr/bin/env python3
"""This  contains a method that rotates a matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """The function that rotates the matrix"""
    # frist transpose the matrix inplace
    row_length = len(matrix)
    matrix.reverse()

    for i in range(row_length):
        for j in range(i + 1, row_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
