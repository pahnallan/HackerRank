# Link to problem https://www.hackerrank.com/challenges/ctci-merge-sort/
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# this is a merge sort but the algoirthm is to  compare left to right and increment
def countInversions(arr):
    result = mergeSort(arr)[1]
    return result


def mergeSort(number_list):
    if len(number_list) == 1:
        return (number_list, 0)

    if len(number_list) == 2:
        if number_list[0] > number_list[1]:
            number_list[0], number_list[1] = number_list[1], number_list[0]
            return (number_list, 1)
        else:
            return (number_list, 0)

    slice_index = math.ceil(len(number_list) / 2)
    left = mergeSort(number_list[0:slice_index])
    right = mergeSort(number_list[slice_index:])

    return_list = []
    return_swap_count = left[1] + right[1]
    # everytime you push the right list items onto the tree while there are items in the left tree, increment by items in the subtree that have not been added to the final list
    len_left = len(left[0])
    len_right = len(right[0])
    left_list = left[0]
    right_list = right[0]
    i = 0
    j = 0
    while i < len_left or j < len_right:
        if i < len_left:
            if j < len_right:
                if left_list[i] <= right_list[j]:
                    return_list.append(left_list[i])
                    i += 1
                else:
                    return_list.append(right_list[j])
                    return_swap_count += (len_left - i)
                    j += 1
            else:
                return_list.append(left_list[i])
                i += 1
        else:
            return_list.append(right_list[j])
            j += 1

    return (return_list, return_swap_count)


if __name__ == '__main__':
    input_list = ["input04.txt"]
    inp = open("input04.txt")
    fptr = open("results04.txt", 'w')

    t = int(inp.readline().strip("\n").strip())

    for t_itr in range(t):
        n = int(inp.readline().strip("\n").strip())

        arr = list(map(int, inp.readline().strip("\n").rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
