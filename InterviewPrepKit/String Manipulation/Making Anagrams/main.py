# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    # a and b are both strings of different lengths
    # My first thought is to create a dictionary for a, and then loop through b to determine what items to delete from dictionary a O(a + b)
    dictionary_a = dict()
    dictionary_b = dict()
    for letter in a:  # O(a)
        dictionary_a[letter] = dictionary_a.get(letter, 0) + 1

    for letter in b:  # O(b)
        dictionary_b[letter] = dictionary_b.get(letter, 0) + 1

    deletions = 0
    for letter in set(list(dictionary_a.keys()) + list(dictionary_b.keys())):  # O(26)
        deletions += abs(dictionary_a.get(letter, 0) - dictionary_b.get(letter, 0))

    return deletions


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
