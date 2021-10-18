#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the rotLeft function below.
# [1,2,3,4,5] 2 -> [3,4,5,1,2]
def rotLeft(a, d):
    array_len = len(a)  # 20, d 10
    offset = d % array_len

    if offset == 0:
        return a

    new_array = []
    for i in range(array_len):
        next_index = (offset + i) % array_len
        print(next_index)
        new_array.append(a[next_index])

    return new_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
