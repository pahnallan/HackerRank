# https://www.hackerrank.com/challenges/find-the-nearest-clone/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#  graph_nodes = 5
#  graph_from = []
#  graph_to = []
#  ids = [] array of integers matching to a "color"
#  val = 1 an integer value representing the color to match

class Vertex:
    def __init__(self, index, color):
        self.index = index
        self.color = color
        self.neighbors = []


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    vertex_list = [Vertex(idx, color) for idx, color in enumerate(ids)]
    connectEdges(graph_from, graph_to, vertex_list)
    shortest_path = -1

    # create a list of indexes to search with
    frontier_vertices = [vertex for vertex in vertex_list if vertex.color == val]

    for starting_frontier_vertex in frontier_vertices:
        frontier = [starting_frontier_vertex]
        result = bfs(frontier, shortest_path)
        if result == -1:
            return -1
        if result < shortest_path or shortest_path == -1:
            shortest_path = result
    return shortest_path


def connectEdges(graph_from, graph_to, vertex_list):
    for i in range(len(graph_from)):
        graph_from_vertex = vertex_list[graph_from[i] - 1]
        graph_to_vertex = vertex_list[graph_to[i] - 1]
        graph_from_vertex.neighbors.append(graph_to_vertex)
        graph_to_vertex.neighbors.append(graph_from_vertex)


def bfs(frontier, shortest_path):
    level_dict = dict()
    level_dict[frontier[0].index] = 0
    level_number = 1
    while frontier:
        next_frontier = []
        for vertext in frontier:
            for neighbor in vertext.neighbors:
                if neighbor.index not in level_dict:
                    level_dict[neighbor.index] = level_number
                    next_frontier.append(neighbor)
                    if neighbor.color == val:
                        return level_number
        level_number += 1
        if shortest_path != -1 and level_number >= shortest_path:
            return shortest_path
        frontier = next_frontier

    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
