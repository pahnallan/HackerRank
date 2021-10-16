# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
# 2, 2, 1, 1, 2 : 2 2: 2, 1: 2
def isValid(s):
    letter_dict = dict()
    for letter in s:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1

    # letter_dict = { a: 3, b: 2, c: 2, d: 3}

    letter_vals = list(letter_dict.values())
    # [4, 2, 2]
    val_dict = dict()
    for val in letter_vals:
        val_dict[val] = val_dict.get(val, 0) + 1

    # val_dict = { 1: 2, 5: 1}
    # val_dic = { 2: 2, 1: 2}
    val_dict_keys_set = list(val_dict.keys())
    if len(val_dict_keys_set) > 2:
        return "NO"
    if val_dict.get(1, 0) == 1:
        val_dict.pop(1)
    val_dict_keys_set = list(val_dict.keys())
    val_list = list(val_dict.values())

    # must check for if
    if len(val_dict_keys_set) > 2:
        return "NO"
    elif len(val_dict_keys_set) == 2:
        if abs(val_dict_keys_set[0] - val_dict_keys_set[1]) > 1:
            return "NO"
        max_count = max(val_dict_keys_set[0], val_dict_keys_set[1])
        if val_dict[max_count] != 1:
            return "NO"
        return "YES"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
