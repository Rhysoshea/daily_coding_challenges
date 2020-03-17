"""
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

- is_locked, which returns whether the node is locked
- lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
- unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""

class Node(object):
    # runs in O(h) time (height of tree) because it is always working upwards, doesn't have to traverse all the children downwards
    # this is achieved by keeping track of how many locked nodes are descendents of each node
    # update the tree above every time a node is locked
    # checking down isn't required but when locking/unlocking we have to check the ancestors

    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.locked = False
        self.parent = parent
        self.left = left
        self.right = right
        self._locked_descendents_count = 0

    def _can_lock_or_unlock(self): # just checks up the ancestors by keeping track of what is below each node
        if self._locked_descendents_count > 0:
            return False

        cur = self.parent
        while cur:
            if cur.locked:
                return False
            cur = cur.parent

        return True

    def is_locked(self):
        return self.locked

    def lock(self):
        if self.locked:
            return False

        if self._can_lock_or_unlock == False:
            return False

        self.locked = True
        cur = self.parent
        while cur:
            cur._locked_descendents_count += 1
            cur = cur.parent

        return True

    def unlock(self):
        if not self.locked:
            return False

        if self._can_lock_or_unlock == False:
            return False

        self.locked = False
        cur = self.parent
        while cur:
            cur._locked_descendents_count =- 1
            cur = cur.parent

        return True
