from queue import Queue

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    height = -1

    q = Queue()
    q.put(root)
    while q.qsize() != 0:
        for i in range(q.qsize()):
            current_node = q.get()
            if current_node.left != None:
                q.put(current_node.left)
            if current_node.right != None:
                q.put(current_node.right)

        height += 1

    return height



