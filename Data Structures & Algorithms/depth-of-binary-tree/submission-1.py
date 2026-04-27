# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # INPUT AND OUTPUT 
        # root 

        # THOUGHT PROCESS
        # define a count variable 
        # so we go to each leaf node and calculate how much depth is the maximum
        # global count, local count
        if not root:
            return 0

        right_count = self.maxDepth(root.right)
        left_count = self.maxDepth(root.left)

        return max(right_count, left_count) + 1


        # EDGE CASES 
        # We can have a root of 0

        