#!/usr/bin/python3
"""This module contains a function for
culculating the parameter of an island in a grid"""


def island_perimeter(grid):
    """function that returns the parameter of
    the island in the provided grid"""

    parameter = 0

    rows = len(grid)
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 1:
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    parameter += 1
                if i + 1 >= rows or grid[i + 1][j] == 0:
                    parameter += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    parameter += 1
                if j + 1 >= cols or grid[i][j + 1] == 0:
                    parameter += 1

    return parameter
