# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        1. INPUT AND OUTPUT
            - height balanced BT is one where the left and right
            - subtrees of very node differ in height by no more than one 


        2. EDGE CASES 
            - root can be None

        3. THOUGHT PROCESS
            - we can task the sub node with taking the difference between its left and right height

        4. STEPS
            - get each sub node to return the height of its children
            - if children height difference is greater than 1 return error
        """
        if not root: 
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))





