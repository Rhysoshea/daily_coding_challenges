"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

"""
More explanation:
Two single linked lists

A = 11 12 13 14 15 16 17 18 19 20
B = 7  8  9  10 12 13 14 15 16 17 18 19 20

The intersecting node is 12, where every node afterwards is the same node in each list.
So we need to line up the 'indices' so we are comparing 1 for 1

Initially both starting pointers will be at the start of each list
Let's shift the pointer of the larger list up by the difference between the length of both lists
So pointer A starts at 11 and pointer B starts at 10, then next both will equal 12 which is the intersecting node

"""

#Node class
class Node:

    def __init__(self,value):
        self.value = value #value of node
        self.next = None

#Linked list class
class LinkedList:

    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print (temp.value)
            temp = temp.next

    def len_list(self,head):
        if not head:
            return 0
        return 1 + self.len_list(head.next)

def build_LinkedList(arr):
    linkedlist = LinkedList()
    for i,val in enumerate(arr):
        if i == 0 :
            last = Node(val)
            linkedlist.head = last
        else:
            last.next = Node(val)
            last = last.next
    return linkedlist



def solution1(A, B):
    # runs in O(N + M) time but uses O(N) space not constant
    a = A.head
    b = B.head

    a_array = [] #O(len(A)) space

    while a: #O(len(A)) time
        a_array.append(a.value)
        a = a.next
    while b: #O(len(B)) time
        if b.value in a_array:
            return b.value
        b = b.next

    return ""

def solution2(A, B):
    #
    a = A.head
    b = B.head

    lenA = A.len_list(a)
    lenB = B.len_list(b)

    if lenA > lenB:
        for _ in range(lenA - lenB):
            a = a.next
    if lenB > lenA:
        for _ in range(lenB - lenA):
            b = b.next

    while a.value != b.value:
        a = a.next
        b = b.next

    return a.value


def test1(A,B, ans):
    assert (solution1(A,B) == ans)

def test2(A,B, ans):
    assert (solution2(A,B) == ans)

A_vals = [3,7,8,10]
B_vals = [99,1,8,10]

A = build_LinkedList(A_vals)
B = build_LinkedList(B_vals)

# A.printlist()
# B.printlist()

print (solution2(A, B))

test1(A,B,8)
test2(A,B,8)
