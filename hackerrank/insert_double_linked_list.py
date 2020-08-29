"""
Given a reference to the head of a doubly-linked list and an integer, data, create a new DoublyLinkedListNode object having data value data and insert it into a sorted linked list while maintaining the sort.

Function Description

Complete the sortedInsert function in the editor below. It must return a reference to the head of your modified DoublyLinkedList.

sortedInsert has two parameters:

1. head: A reference to the head of a doubly-linked list of DoublyLinkedListNode objects.
2. data: An integer denoting the value of the data field for the DoublyLinkedListNode you must insert into the list.
Note: Recall that an empty list (i.e., where head=null) and a list with one element are sorted lists.

Input Format

The first line contains an integer n, the number of test cases.

Each of the test case is in the following format:

The first line contains an integer , the number of elements in the linked list.
Each of the next n lines contains an integer, the data for each node of the linked list.
The last line contains an integer data which needs to be inserted into the sorted doubly-linked list.
"""
For your reference:

class DoublyLinkedListNode:
    
    def __init__(self, data):
    self.data =  data
    self.next = None
    self.prev = None



def sortedInsert(head, data):

    if not head:
        return DoublyLinkedListNode(data)

    current = head
    while current.next:
        if data <= current.next.data:
            break
        else:
            current = current.next

    if data < current.data:
        node = DoublyLinkedListNode(data)
        node.next = current
        head = node
    else:
        node = DoublyLinkedListNode(data)
        node.next = current.next
        current.next = node

    return head
