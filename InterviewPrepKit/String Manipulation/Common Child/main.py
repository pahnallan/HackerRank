# https://www.hackerrank.com/challenges/common-child/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Solution implemented with tabulation
def commonChild(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)

    table = [[None] * (s2_len + 1) for i in range(s1_len + 1)]

    for i in range(s1_len + 1):
        for j in range(s2_len + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i][j - 1], table[i - 1][j])

    return table[s1_len][s2_len]



# Naive solution
def lcs(s1, s2, memo):
    memo_key = "{},{}".format(s1, s2)
    print(memo_key)
    if memo_key in memo:
        print("Cache Hit on {}".format(memo_key))
        return memo[memo_key]

    s1_len = len(s1)
    s2_len = len(s2)
    if s1_len == 0 or s2_len == 0:
        return 0

    if s1[-1] == s2[-1]:
        memo[memo_key] = 1 + lcs(s1[0: s1_len - 1], s2[0: s2_len - 1], memo)
    else:
        memo[memo_key] = max(lcs(s1[0: s1_len - 1], s2, memo), lcs(s1, s2[0: s2_len - 1], memo))

    return memo[memo_key]


if __name__ == '__main__':
    inp = open("input04.txt")
    fptr = open("results04.txt", 'w')

    _s1 = inp.readline().strip("\n")

    _s2 = inp.readline().strip("\n")

    result = commonChild(_s1, _s2)

    fptr.write(str(result) + '\n')

    fptr.close()
