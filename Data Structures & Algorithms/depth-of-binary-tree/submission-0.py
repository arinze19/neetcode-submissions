# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # INPUT AND OUTPUT 
        # root 

        # THOUGHT PROCESS
        # 


        # EDGE CASES 
        # We can have a root of 0

        if not root:
            return 0

        queue = [root]
        level = 0


        while queue:
            # loop through the items in the queue
            # add them to a new queue
            local_queue = []
            level += 1

            for item in queue:
                if item.right:
                    local_queue.append(item.right)

                if item.left:
                    local_queue.append(item.left)

            queue = local_queue

        return level