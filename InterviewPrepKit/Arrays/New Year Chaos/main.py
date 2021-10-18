# https://www.hackerrank.com/challenges/new-year-chaos/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    q = [p - 1 for p in q]
    bribeCounter = 0
    for i in range(len(q)):
        if q[i] > i + 2:
            bribeCounter = "Too chaotic"
            break

        for j in range(max(0, q[i] - 1), i):
            if q[j] > q[i]:
                bribeCounter += 1

    print(bribeCounter)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
