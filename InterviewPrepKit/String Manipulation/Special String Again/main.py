# https://www.hackerrank.com/challenges/special-palindrome-again/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the substrCount function below.
def substrCount(n, s):
    l = []
    count = 0
    cur = None

    # 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0

    # 2nd pass
    for i in l:
        ans += sum([i for i in range(1, i[1] + 1)])

    # 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans


def substrCount2(n, s):
    count = 0
    for index in range(n):
        for inner_index in range(index + 1, n + 1):
            if isSpecial(s[index:inner_index]):
                count += 1
    return count


def isSpecial(substring):
    print(substring)
    substring_len = len(substring)
    if substring_len == 1:
        return True

    const_letter = substring[0]
    j = substring_len
    for i in range(substring_len):
        j -= 1
        if i >= j:
            return True

        if substring[i] != const_letter or substring[j] != const_letter:
            return False

    return False


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
