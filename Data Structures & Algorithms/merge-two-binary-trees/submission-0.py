# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # does the follow the normal 2i + 1 | 2i + 2 format?
        # number of nodes in tree can be 0 | so we can have a null root for either 

        # handle empty cases 
        if not root1 and not root2:
            return None

        if not root1:
            return root2

        if not root2:
            return root1

        total = root1.val + root2.val

        node = TreeNode(total)

        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)

        return node

        # [1,3,2] [2,1,3]