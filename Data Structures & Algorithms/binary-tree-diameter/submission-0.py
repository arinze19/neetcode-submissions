# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # INPUT AND OUTPUT
        # root cannot be empty
        # min val = -100 and max val = 100

        # THOUGHT PROCESS
        # length of the longest path between two nodes
        height = [0]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            height[0] = max(height[0], left + right)

            return 1 + max(left, right) # return diamter

        dfs(root)  # get height

        return height[0]  # return max height
