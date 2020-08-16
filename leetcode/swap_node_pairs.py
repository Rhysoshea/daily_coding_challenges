"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def generateLinkedList(arr):
    start = curr = ListNode(0)
    for i in arr:
        curr.next = ListNode(i)
        curr = curr.next

    return start.next

def printList(head):
    while head:
        print(head.val)
        head = head.next
    print ("\n")

class Solution:

    def __init__(self, dummy):
        self.dummy = dummy 

    def swapPairs(self, head):
        if not head:
            return None

        curr = head 
        temp = ListNode(0)
        temp.next = head
        pre = temp
        while curr and curr.next:
            pre.next  = curr.next
            pre = pre.next 
            curr.next = pre.next
            pre.next = curr 
            pre = curr 
            curr = curr.next

        return temp.next



solve = Solution(0)

arr = [1,2,3,4]
arr = generateLinkedList(arr)

solution = [2,1,4,3]
solution = generateLinkedList(solution)

assert(printList(solve.swapPairs(arr)) == printList(solution))


arr = [1, 5, 6, 4, 3, 2]
arr = generateLinkedList(arr)

solution = [5, 1, 4, 6, 2, 3]
solution = generateLinkedList(solution)

assert(printList(solve.swapPairs(arr)) == printList(solution))
