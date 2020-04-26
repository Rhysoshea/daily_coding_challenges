# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

# You are given pointer to the root of the binary search tree and two values v1 and v2. You need to return the lowest common ancestor (LCA) of v1 and v2 in the binary search tree.


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
# def dfs(root, v1, v2, v1_found, v2_found, l):
#     if not root:
#         l.append(-1)
#     else:
#         l.append(root.info)
#     if root:
#         if root.info == v1:
#             v1_found = True 
#         if root.info == v2:
#             v2_found == True 
#     if v1_found and v2_found:
#         return l
#     if root:
#         left = dfs(root.left, v1, v2, v1_found, v2_found, l)
#         right = dfs(root.right, v1, v2, v1_found, v2_found, l)
#         l.extend(left)
#         l.extend(right)
#         return l


# Solution:
# this is a binary search tree so everything to the left < current and right > current 
# so current root will either be less than or greater than both v1 and v2
# when it is in between then that is the common ancestor

def lca(root, v1, v2):
  #Enter your code here

    if(root.info < v1 and root.info < v2):
        return lca(root.right,v1,v2)
    if(root.info > v1 and root.info > v2):
        return lca(root.left,v1,v2)

    return root



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
