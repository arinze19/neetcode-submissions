# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # INPUT AND OUTPUT 
        # root could be empty
        # max nodes of 100 nodes 

        # THOUGHT PROCESS
        # return [] if root is not available
        # add root to a queue
        # for the queue, get the right most item
        # clear the queue
        # add the children of each item into the queue
        # repeat

        # EDGE CASES
        res = []

        if not root:
            return res

        stack = [root]

        while stack:
            # fetch the last item and add it to the res
            top = stack[-1]
            children = []

            res.append(top.val)

            # for each item in the stack, append the children
            for node in stack:
                if node.left:
                    children.append(node.left)

                if node.right:
                    children.append(node.right)

            stack = children

        return res


