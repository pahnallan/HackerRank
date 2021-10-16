# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem
#!/bin/python3

import math
import os
import random
import re
import sys
import bisect


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    # Write your code here
    cost_window_unordered = []
    cost_window_list = []
    total_notifications = 0
    a = None
    b = math.floor(d / 2)

    if d % 2 == 0:
        a = b - 1

    for i, cost in enumerate(expenditure):
        if i > d - 1:
            median = getMedian(cost_window_list, a, b)
            cost_window_list.pop(bisect.bisect_left(cost_window_list, cost_window_unordered.pop(0)))
            if cost >= median * 2:
                total_notifications += 1

        bisect.insort(cost_window_list, cost)
        cost_window_unordered.append(cost)
    return total_notifications


def getMedian(trailing_cost_list, a, b):
    if a is None:
        return trailing_cost_list[b]
    else:
        return (trailing_cost_list[a] + trailing_cost_list[b]) / 2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
