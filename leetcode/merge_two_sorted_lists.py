"""

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
Accepted
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__():
        pass 

    def mergeTwoLists(l1, l2):
        """
        use nodes in place as they are
        create a new list by referencing nodes in order
        """
        p = l3 = ListNode(0)
 
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next 
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        l3.next = l1 or l2 # collects remaining nodes of any lists that aren't fully referenced

        return p.next


solve = Solution

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# solve.mergeTwoLists(l1,l2)

l1 = None 
l2 = ListNode()
print(solve.mergeTwoLists(l1,l2))