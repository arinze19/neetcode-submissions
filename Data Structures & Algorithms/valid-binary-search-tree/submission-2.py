# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # INPUT AND OUTPUT
        # strictly greater than and less than
        # min number of nodes = 1
        # max number of nodes = 1000

        # THOUGHT PROCESS
        # dfs from bottom to top
        # [True, max/min value of the tree]
        def dfs(node, left, right):
            if not node:
                return True
            
            if not node.val < right or not node.val > left:
                return False
            
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))
