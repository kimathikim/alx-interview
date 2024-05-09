#!/usr/bin/python3
"""This module contains a function for
culculating the parameter of an island in a grid"""


def island_perimeter(grid):
    """this function eturns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside
that isn’t connected to the water surrounding the island).
"""
    parameter = 0

    rows = len(grid)
    for i in range(rows):
        cols = len(grid[i])
        for j in range(cols):
            if grid[i][j] == 1:
                if grid[i][j+1] == 0 and grid[i][j-1] == 0:
                    if grid[i-1][j] == 0 or grid[i+1][j] is None:
                        parameter += 3
                        continue
                    parameter += 3

                if grid[i-1][j] == 0 and grid[i+1][j] == 0:
                    if grid[i][j+1] == 0 or grid[i][j-1] == 0:
                        parameter += 3
                        continue
                if grid[i][j+1] == 1 and grid[i][j-1] == 1:
                    if grid[i-1][j] == 0 and grid[i+1][j] == 1:
                        parameter += 1
                        continue
                    if grid[i-1][j] == 1 and grid[i+1][j] == 0:
                        parameter += 1
                        continue
                    parameter += 0
                if grid[i-1][j] == 1 and grid[i+1][j] == 1:
                    if grid[i][j+1] == 0 and grid[i][j-1] == 1:
                        parameter += 1
                        continue
                    if grid[i][j+1] == 1 and grid[i][j-1] == 0:
                        parameter += 1
                        continue
                    parameter += 0
                parameter += 2
    return parameter
