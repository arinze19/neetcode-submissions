# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        Keywords
        1. value greater than x 
        
        Questions 
        1. can node be empty? No
        2. max values for nodes (-100, 100) 

        Thought Process
        1. keep track of largest int so far for each path
        '''

        def dfs(node, val):
            # base case 
            if not node:
                return 0

            left = dfs(node.left, max(node.val, val))
            right = dfs(node.right, max(node.val, val))

            
            count = 1 if node.val >= val else 0

            return count + left + right
        
        return  dfs(root, -101)

        
        