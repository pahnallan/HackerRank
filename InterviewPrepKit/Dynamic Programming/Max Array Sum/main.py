#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_sum = 0
    memo = dict()
    for i in range(len(arr)-1, -1, -1):
        print("I is {}".format(i))
        result = maxSubsetRecurse(arr, i, memo)
        if result > max_sum:
            max_sum = result
    return max_sum

def maxSubsetRecurse(arr, index, memo):
    if index in memo:
        return memo[index]
    len_arr = len(arr)
    next_start_index = index + 2
    if next_start_index >= len_arr:
        memo[index] = arr[index] if index + 1 >= len_arr or arr[index] > arr[index + 1] else arr[index + 1]
        return memo[index]

    subset_result = maxSubsetRecurse(arr, next_start_index, memo)
    if index + 1 >= len_arr:
        memo[index] = arr[index] + subset_result if subset_result > 0 else 0
    else:
        memo[index] = max(arr[index] + (subset_result if subset_result > 0 else 0), memo[index + 1])
    return memo[index]


if __name__ == '__main__':
    inp = open("input00.txt")
    fptr = open("results00.txt", 'w')

    n = int(inp.readline().strip("\n"))

    arr = list(map(int, inp.readline().strip("\n").rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
