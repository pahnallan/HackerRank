# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#  0, 1, 2, 3
#

def insertNodeAtPosition(llist, data, position):
    insert_data = SinglyLinkedListNode(data)
    if position == 0:
        insert_data.next = llist
        llist = insert_data
    else:
        previous_node = llist
        current_node = llist.next
        while (position > 1 and current_node is not None):
            position -= 1
            previous_node = current_node
            current_node = current_node.next


    insert_data.next = current_node
    previous_node.next = insert_data

    return llist

