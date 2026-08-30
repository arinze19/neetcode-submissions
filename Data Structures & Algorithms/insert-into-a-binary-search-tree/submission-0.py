# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        keywords
        1. 

        Questions 
        1. root value does not exist in the tree | special case | if not node return NodeVal
        2. root can be empty
        3. values in tree are unique

        Thought process 
        - empty list 
        - leaf node 
        - internal node 
        1. bottom-up/
            - create new nodes 
            - get the min/max of both branches
            - left = dfs(node.left)
            - right = dfs(node.right)

            dfs(root, node):
                - base case 
                if not root:
                    return node

                - recursive case (success)
                if root.val < node.val:
                    root.right = dfs(root.right, node)

                if root.val > node.val:
                    root.left = dfs(root.left, node) 

                return root
                
            return dfs(root, node)

        Time and Space 
        1. time | O(log n)
        2. space | O(1)
        '''

        node = TreeNode(val)

        def dfs(root, node):
            if not root:
                return node

            if root.val < node.val:
                root.right = dfs(root.right, node)

            if root.val > node.val:
                root.left = dfs(root.left, node)

            return root

        return dfs(root, node)