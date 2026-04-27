# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # INPUT AND OUTPUT
        res = [0] # TODO: why do we need to do this??


        def dfs(root: TreeNode, maximum: int):
            # if not root, return
            if not root:
                return None

            # if root.val > maximum
            # increment res
            # set current maximum = root.val
            if root.val >= maximum:
                res[0] += 1
                maximum = root.val

            # run logic across left and right children
            dfs(root.left, maximum)
            dfs(root.right, maximum)

        dfs(root, float("-inf"))

        return res[0]