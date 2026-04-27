# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # INPUT AND OUTPUT 
        # our root can be empty

        # THOUGHT PROCESS
        # do a bfs
        # for each level, create a new array
        # if array is empty at the end of level, do not add it to the result
        res = []

        if not root:
            return res

        queue = deque([root])

        while queue:
            local_list = []
            children = []

            while queue:
                top = queue.popleft()

                # add item
                local_list.append(top.val)

                if top.left:
                    children.append(top.left)

                if top.right:
                    children.append(top.right)
            
            res.append(local_list)

            queue.extend(children)

        return res