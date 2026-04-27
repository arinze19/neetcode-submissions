"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # if not root: return 
        # queue?
        # pop from the back like a stack??
        # use appendleft to keep in track
        if not root:
            return 

        queue = deque([root])

        while queue:
            length = len(queue)
            prev = None

            for i in range(length):
                top = queue.pop()

                top.next = prev

                prev = top

                if top.right:
                    queue.appendleft(top.right)

                if top.left:
                    queue.appendleft(top.left)
        
        return root
                



        