# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem
class Node:
    def __init__(self, index):
        self.index = index
        self.neighbors = []


class Graph:
    def __init__(self, n):
        self.graph_list = [Node(idx) for idx in range(n)]

    def connect(self, x, y):
        self.graph_list[x].neighbors.append(self.graph_list[y])
        self.graph_list[y].neighbors.append(self.graph_list[x])

    def find_all_distances(self, starting_node):
        # Create a list of n size with -1 values
        distance_results = [-1 for _ in range(len(self.graph_list))]
        parent = dict()

        parent[starting_node] = None
        frontier = [self.graph_list[starting_node]]
        next_frontier = []

        level = 1

        while frontier:
            for node in frontier:
                for neighbor in node.neighbors:
                    if neighbor.index not in parent:
                        parent[neighbor.index] = node
                        distance_results[neighbor.index] = level * 6
                        next_frontier.append(neighbor)
            level += 1
            frontier = next_frontier
            next_frontier = []

        print(" ".join([str(xx) for idx, xx in enumerate(distance_results) if idx != starting_node]))


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
