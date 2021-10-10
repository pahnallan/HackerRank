# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check(root, minimum_value, maximum_value):
    if root == None:
        return True
    elif root.data <= minimum_value or root.data >= maximum_value:
        return False
    else:
        return check(root.left, minimum_value, root.data) and check(root.right, root.data, maximum_value)

def checkBST(root):
    return check(root, -1, 10001)