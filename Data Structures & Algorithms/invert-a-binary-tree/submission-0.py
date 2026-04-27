# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # INPUT AND OUTPUT 
        # do we want to create a brand new tree? 
        # do we modify in place??

        # THOUGHT PROCESS
        # we can use a BFS to modify by level
        # update using a reverse 
        

        # EDGE CASES 
        # null roots? 
        # if null roots just return null
        queue = [root]

        while queue:
            # temp = top item.left
            # point top item.left = item.right
            # point top item.right = temp
            item = queue.pop(0)

            if not item:
                continue

            temp = item.left

            item.left = item.right
            item.right = temp

            queue += [item.right, item.left]
        
        return root

