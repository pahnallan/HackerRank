# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# -7, 0, 3
# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    minimum = abs(arr[0] - arr[1])
    for index, number in enumerate(arr):
        current_diff = abs(number - arr[index + 1])
        if current_diff < minimum:
            minimum = current_diff

        if index + 2 == len(arr):
            return minimum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
