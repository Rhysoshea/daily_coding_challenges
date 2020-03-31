'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
All the leaves and the 1s
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

NOTE: leaves count as unival since both sides are nothing
 '''
from binarytree import tree
from binarytree import Node

# A binary tree node
# class Node(object):
#
#     def __init__(self, value, left=None, right=None):
#         self.value = value  # The node value
#         self.left = left    # Left child
#         self.right = right  # Right child

# Driver program to test above function
root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.left.left = Node(1)
root.left.right = Node(1)
root.right.right = Node(0)
root.right.left = Node(1)
root.right.left.left = Node(1)
root.right.left.right = Node(1)
print (root)
# exit()

'''
O(n**2) time since every node in the subtree is being evaluated again
'''

def is_unival(root):
    return unival_helper(root, root.value)

def unival_helper(root, value):
    if root is None:
        return True
    if root.value == value:
        return unival_helper(root.left, value) and unival_helper(root.right, value)
    return False

def unival_counter(root):
    if root is None:
        return 0
    left = unival_counter(root.left)
    right = unival_counter(root.right)

    return 1 + left + right if is_unival(root) else left + right

# print (unival_counter(root))
# print (root)

'''
O(n) time, by starting from the leaves instead of the root
'''

def count_unival(root):
    count,_ = helper(root)
    return count

def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False

print (count_unival(root))
# print (root)
