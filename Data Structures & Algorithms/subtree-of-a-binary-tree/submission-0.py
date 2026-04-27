# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # INPUT AND OUTPUT 
        # root node could also be considered as a root of itself 
        # there is going to be at least one node on the root

        # THOUGHT PROCESS
        # create a helper function to determine if a node is same as another 
        # loop through each node in "root" and check 
        """
        if (root.val == subRoot.val and self.isSame(root, subRoot)):
            return True

        we end our search after we are done with our nodes
        """
        # TODO
        # create a helper function that validates if two trees are the same [done]
        # scan through root node and validate check when root.val == subRoot.val (BFS)
        queue = deque([root])

        while queue:
            top = queue.popleft()

            if top.val == subRoot.val and self.isSame(top, subRoot):
                return True

            if top.right:
                queue.append(top.right)

            if top.left:
                queue.append(top.left)


        return False

    
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if node1 and not node2 or node2 and not node1:
                return False

            if not node1 and not node2:
                return True

            if node1.val != node2.val:
                return False

            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            
        return dfs(root, subRoot)