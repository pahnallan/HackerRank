# https://www.hackerrank.com/challenges/2d-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    cache = []

    maxSum = None

    for y in range(4):
        for x in range(4):
            hourglassSum = calculateHourGlassSum(arr, x, y)
            cache.append(hourglassSum)
            if (maxSum == None or hourglassSum > maxSum):
                maxSum = hourglassSum

    return maxSum


def calculateHourGlassSum(arr, y, x):
    hourGlass0 = arr[y][x] + arr[y][x + 1] + arr[y][x + 2]
    hourGlass1 = arr[y + 1][x + 1]
    hourGlass2 = arr[y + 2][x] + arr[y + 2][x + 1] + arr[y + 2][x + 2]
    return hourGlass0 + hourGlass1 + hourGlass2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
