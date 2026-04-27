# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # INPUT AND OUTPUT
        # root can be empty
        # min -1000 and max 1000
        
        # if we get the parent from the args,
        # we can add args + node.val == target:
        

        # what is the input of our helper [node, count (sum of the parent node values)]
        # - if not node:
        #   - return False
        # - if not node.left and not node.right and node.val + count == targetSum
        #   - return True
        # - return dfs(node.left, count + node.val) or dfs(node.right, count + node.val)
        # what is the return output of our helper
        #   - we need to return a boolean

        def dfs(node, count):
            if not node:
                return False

            if not node.left and not node.right and node.val + count == targetSum:
                return True

            return dfs(node.left, count + node.val) or dfs(node.right, count + node.val)


        return dfs(root, 0)