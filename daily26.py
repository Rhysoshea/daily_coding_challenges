"""
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

e.g.
List   K:3              3   2   1   0th last
1   2   3   4   5   6   7   8   9   10


"""
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        a = []
        while temp:
            a.append(temp.value)
            temp = temp.next
        print (a)

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

def solution(input, k):
    pointer = input.head
    k_pointer = input.head


    for _ in range(k):
        k_pointer = k_pointer.next

    while k_pointer.next:
        last_pointer = pointer
        pointer = pointer.next
        k_pointer = k_pointer.next

    last_pointer.next = pointer.next
    return input

def test(input, k, ans):
    assert (solution(input, k) == ans)



A = [1,2,3,4,5,6,7,8,9,10]

llist = build_LinkedList(A)

k = 3
llist.printlist()

new_list = solution(llist, k)

new_list.printlist()

# test(llist,k,[1, 2, 3, 4, 5, 6, 8, 9, 10])
