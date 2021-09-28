# https://www.hackerrank.com/challenges/alternating-characters/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    deletions = 0
    previous_letter = s[0]
    for letter in s[1:]:
        if letter == previous_letter:
            deletions += 1
        else:
            previous_letter = letter
    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
