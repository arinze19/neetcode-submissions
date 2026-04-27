# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # INPUT AND OUTPUT
        # the left side should be equivalent to the right part?
        # DFS or BFS
        # BFS: 
        # enqueue the node; check if it matches
        # if so, validate children 
        # if not, return false
        # recursive DFS
        if not p and not q:
            return True

        if getattr(p, "val", None) != getattr(q, "val", None):
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

