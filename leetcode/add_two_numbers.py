# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class listNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

    def print_list(self):
        print (self.val)
        if self.next != None:
            self.next.print_list()

def addRemaining(llist):
    while True:
        output.next = listNode(llist.val)
        if llist.next ==None:
            break
    return 0

def addTwoNumbers(llist1, llist2):
    carry = 0
    output = listNode(None)
    while True:
        s = llist1.val + llist2.val + carry 
        # print(s)
        carry = 0
        if s >= 10:
            carry += 1
            s = s%10
        
        if output.val == None:
            output = listNode(s)
            firstNode = output
        else:
            output.next = listNode(s)
            output = output.next

        if llist1.next == None and llist2.next == None:
            break

        llist1 = llist1.next
        llist2 = llist2.next

    if llist1.next == None and llist2.next != None:
        while True:
            output.next = listNode(llist2.val)
            output = output.next
            if llist2.next == None:
                break
    if llist1.next != None and llist2.next == None:
        while True:
            output.next = listNode(llist1.val)
            output = output.next
            if llist1.next == None:
                break
    return firstNode




llist1 = listNode(2)
llist1.next = listNode(4)
llist1.next.next = listNode(3)

# 2 -> 4 -> 3 represents 342

# print(llist1.next.next.next.val)

# llist1.print_list()

llist2 = listNode(5)
llist2.next = listNode(6)
llist2.next.next = listNode(4)

# 5 -> 6 -> 4 represents 465

ans = addTwoNumbers(llist1, llist2)
ans.print_list()
