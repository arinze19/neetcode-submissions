# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # INPUT AND OUTPUT 
        # kth smallest value in the tree
        
        # THOUGHT PROCESS
        # we can do a pre-order traversal to get the nodes sorted in an array
        # get the k + 1 value

        res = []

        def dfs(node):
            # pre-order traversal
            if not node:
                return 

            # process left
            dfs(node.left)

            # process current 
            res.append(node.val)

            # proceess right
            dfs(node.right)

        dfs(root)

        return res[k - 1]