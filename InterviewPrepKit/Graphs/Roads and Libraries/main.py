# https://www.hackerrank.com/challenges/torque-and-development/problem
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#
class Node:
    def __init__(self, index):
        self.index = index
        self.visited = False
        self.neighbors = []


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Return minimal cost
    if c_road >= c_lib:
        return c_lib * n

    graph_list = [Node(idx) for idx in range(n)]

    for x, y in cities:
        graph_list[x - 1].neighbors.append(graph_list[y - 1])
        graph_list[y - 1].neighbors.append(graph_list[x - 1])

    # visit every node at least once. do a Depth first traversal on each node if that node ws not previously visited. The

    total_minimum_cost = 0
    for node in graph_list:
        if not node.visited:
            result = dfs(node)  # returns amt of cities connected in this tree
            total_minimum_cost += ((result - 1) * c_road + c_lib)

    return total_minimum_cost


def dfs(node):
    node.visited = True
    if not node.neighbors:
        return 1

    return_city_count = 1
    for neighbor in node.neighbors:
        if not neighbor.visited:
            return_city_count += dfs(neighbor)
    return return_city_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
