# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Keywords
        1. p and q
        2. nodes can be descendants of themselves

        Questions 
        1. values in root are unique
        2. 

        Thought process 
        1. bottom-up 
        -> None | value

        - if not node:
            * return None
        - if isinstance(left, int) and isinstance(right, int) or node == p or node == q:
            * return node
        - if left:
            * return left 
        - if right:
            * return right
        - return None

        Time and Space 
        time | O(n)
        space | O(n)
        '''
        def dfs(node: 'TreeNode'):
            if not node:
                return float('inf')

            left = dfs(node.left)
            right = dfs(node.right)

            
            if (left != float('inf') and right != float('inf')) or node.val == p.val or node.val == q.val:
                return node
            
            if left != float('inf'):
                return left

            if right != float('inf'):
                return right

            
            return float('inf')

        return dfs(root)


