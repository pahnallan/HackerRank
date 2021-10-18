# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

# !/bin/python3

import math
import os
import random
import re
import sys
import heapq


# Complete the minimumSwaps function below.
# [3,2,6,7]
# [1,3,5,4,2,6,7]
# [1,2,5,4,3,6,7]
# [1,2,3,4,5,6,7]

def minimumSwaps(arr):
    array_length = len(arr)
    swap_count = 0
    heapified_list = []
    mydict = dict()
    for index, num in enumerate(arr):
        heapified_list.append(num)
        mydict[num] = index

    heapq.heapify(heapified_list)

    for index in range(len(arr)):
        root_item = heapified_list[0]
        if root_item < arr[index]:
            index_of_root = mydict[root_item]

            # change the index of the bigger item  to the index of the smaller item
            arr[index_of_root] = arr[index]
            mydict[arr[index]] = index_of_root

            heapq.heappop(heapified_list)
            swap_count += 1
        else:
            heapq.heappop(heapified_list)

    return swap_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
