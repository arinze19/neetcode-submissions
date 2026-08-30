# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        KEYWORDS
        1. 

        QUESTIONS 
        1. duplicate values in the tree? No
        2. tree balanced? No
        3. can tree be empty? No
        4. can low and high be same? Yes 

        SPACE AND TIME 
        1. time | O(n)
        2. space | O()
        ''' 
        res = 0

        def dfs(node):
            nonlocal res 

            # base case 
            if not node:
                return 
            
            # recursive case (success)
            if node.val >= low and node.val <= high:
                res += node.val

            dfs(node.right)
            dfs(node.left)

        dfs(root)

        return res 