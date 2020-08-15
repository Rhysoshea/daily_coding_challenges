"""
Given an array of linked-lists, each linked list is sorted in ascending order.

Merge all the linked-lists into one sort linked-list and return it.
 

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

"""
# Solution combines merge sort algorithm and method to sort 2 linked lists


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, dummy):
        self.dummy = dummy 


    def printLList(self, arr):
        for node in arr:
            while node:
                print(node.val)
                node = node.next
            print ("\n")

    def mergeKLists(self, lists):

        def merge2Lists(l1, l2):
            startNode = curr = ListNode(0)  # beginning of output
            # print (l1.val)
            # print (l2.val)
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            curr.next = l1 or l2  #allocates the rest of whichever list remains
            return startNode.next #drops the first 0 node

        def mergeSort(arr):
            if not arr:
                return None
            if len(arr) < 2:
                return arr[0] 
            if len(arr)==2:
                return merge2Lists(arr[0], arr[1])

            n = len(arr)//2
            # print ("left")
            # self.printLList(arr[:n])
            # print ("right")
            # self.printLList(arr[n:])

            left = mergeSort(arr[:n])
            right = mergeSort(arr[n:])
            return merge2Lists(left, right)

        if len(lists)<1:
            return None
        return mergeSort(lists)


def LListGenerator(listsArr):
    # takes an array of lists of integers and returns an array of linked lists
    lists = []

    for l in listsArr:
        startNode = node = None
        for i in range(len(l)):
            if not node:
                startNode = node = ListNode(l[i])
            else:
                node.next = ListNode(l[i])
                node = node.next

        lists.append(startNode)

    return lists

def printLList(node):
    while node:
        print (node.val)
        node = node.next
    print ("\n")


solve = Solution(0)


listsArr = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = LListGenerator(listsArr)

solutionArr = [[1, 1, 2, 3, 4, 4, 5, 6]]
solution = LListGenerator(solutionArr)

assert(printLList(solve.mergeKLists(lists)) == printLList(solution[0]))


listsArr = []
lists = LListGenerator(listsArr)

solutionArr = []
solution = LListGenerator(solutionArr)

assert(printLList(solve.mergeKLists(lists)) == printLList(solution))


listsArr = [[]]
lists = LListGenerator(listsArr)

solutionArr = []
solution = LListGenerator(solutionArr)

assert(printLList(solve.mergeKLists(lists)) == printLList(solution[0]))


listsArr = [[-10, -9, -9, -3, -1, -1, 0], [-5], [4], [-8],
            [], [-9, -6, -5, -4, -2, 2, 3], [-3, -3, -2, -1, 0]]
lists = LListGenerator(listsArr)


solutionArr = [[-10, -9, -9, -9, -8, -6 ,-5, -5, -4, -3, -3, -3, -2, -2, -1, -1, -1, 0, 0, 2, 3, 4]]
solution = LListGenerator(solutionArr)

assert(printLList(solve.mergeKLists(lists)) == printLList(solution[0]))
