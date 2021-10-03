# https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maxRegion' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def maxRegion(grid):
    largest_cell = -1
    parent = {}
    row_max = len(grid)
    column_max = len(grid[0])
    for row in range(row_max):
        for column in range(column_max):
            if grid[row][column] == 1 and "{},{}".format(row, column) not in parent:
                print("Starting")
                result = recurseGraph(grid, row, column, parent, row_max, column_max)
                if result != 0 and result > largest_cell:
                    largest_cell = result
    return largest_cell


def recurseGraph(grid, row, column, parent_dictionary, row_max, column_max):
    cell_key = "{},{}".format(row, column)
    if cell_key in parent_dictionary:
        return 0
    parent_dictionary[cell_key] = True
    if row_max <= row or row < 0 or column_max <= column or column < 0 or grid[row][column] == 0:
        return 0

    return 1 + sum([recurseGraph(grid, xrow, xcolumn, parent_dictionary, row_max, column_max) for xrow in range(row - 1, row + 2) for xcolumn in range(column - 1, column + 2) if
                    not (xrow == row and xcolumn == column)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
