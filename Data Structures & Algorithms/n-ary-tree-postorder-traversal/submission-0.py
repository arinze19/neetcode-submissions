"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''
        Questions 
        1. 
        '''
        res = []

        if not root:
            return res

        
        def dfs(node):
            nonlocal res 

            # base case 
            if not node.children:
                res.append(node.val)
                return

            for child in node.children:
                dfs(child)

            res.append(node.val)

        dfs(root)

        return res

