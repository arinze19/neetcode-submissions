# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''
        KEYWORDS
        1. leaf node 
        2. return node
        3. if is leaf (if not right and not left and node.val == target)

        THOUGHT PROCESS
        1. 
        '''

        def dfs(node):
            # base case 
            if not node:
                return None

            # if node is target and leaf 
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if not node.right and not node.left and node.val == target:
                return None

            return node

        return dfs(root)
