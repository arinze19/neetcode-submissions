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
        - we can have None root
        - max n of 1000

        2. EDGE CASES 

        3. THOUGHT PROCESS
            - what makes a node balanced
                * children have equal height 
        4. TASKS
            - write a recursive call to return the height of a particular node [done]
            - how to write algorithms that check the balance of the node??
        """

        def dfs(node):
            # handle None value
            if not node:
                return [True, 0]

            # get left and right height
            left = dfs(node.left) # [True, 1]
            right = dfs(node.right) # [True, 2]
            
            # return value
            return [right[0] and left[0] and abs(left[1] - right[1]) <= 1,  1 + max(left[1], right[1])]

        return dfs(root)[0]
        





