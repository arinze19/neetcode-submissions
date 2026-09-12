from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])
        level = 0

        if not root:
            return res

        while queue:
            children = []
            level_length = len(queue)

            for _ in range(level_length):
                top = queue.popleft()

                children.append(top.val)

                if top.left:
                    queue.append(top.left)
                
                if top.right:
                    queue.append(top.right)

                
            if level % 2 != 0:
                children.reverse() # reverse children

            res.append(children)
            level += 1

        return res


            


        