# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

    def print_list(self):
        print (self.val)
        if self.next != None:
            self.next.print_list()


def addTwoNumbers(llist1, llist2):
    carry = 0
    output = ListNode(None)
    while True:
        s = llist1.val + llist2.val + carry 
        carry = 0
        if s >= 10:
            carry += 1
            s = s%10
        
        if output.val == None:
            output = ListNode(s)
            firstNode = output
        else:
            output.next = ListNode(s)
            output = output.next

        if llist1.next == None or llist2.next == None:
            break

        llist1 = llist1.next
        llist2 = llist2.next

    if llist1.next == None and llist2.next != None:
        llist2 = llist2.next
        while True:
            s = llist2.val + carry 
            carry = 0
            if s >= 10:
                carry = 1
                s = s %10
            output.next = ListNode(s)
            output = output.next
            if llist2.next == None:
                break
            llist2 = llist2.next 

    elif llist1.next != None and llist2.next == None:
        llist1 = llist1.next
        while True:
            s = llist1.val+carry
            print ('here')
            print (s)
            carry = 0
            if s >= 10:
                carry = 1
                s = s % 10
            output.next = ListNode(s) 
            output = output.next
            if llist1.next == None:
                break
            llist1 = llist1.next

    if carry != 0:
        output.next = ListNode(carry)
    
    return firstNode




llist1 = ListNode(1)
llist1.next = ListNode(8)
# llist1.next.next = ListNode(3)

# 2 -> 4 -> 3 represents 342

# print(llist1.next.next.next.val)

# llist1.print_list()

llist2 = ListNode(0)
# llist2.next = ListNode(6)
# llist2.next.next = ListNode(4)
# llist2.print_list()

# 5 -> 6 -> 4 represents 465

ans = addTwoNumbers(llist1, llist2)
ans.print_list()
