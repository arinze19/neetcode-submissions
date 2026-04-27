# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # INPUT AND OUTPUT 
        # preorder [1,2,3]
        # inorder [2,1,3]
        # empty list [there is no empty list] 
        # unique values [no]

        # while i < preorder
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid]) # why use mid + 1
        # for the inorder I can understand we want to take the items to the left
        root.right = self.buildTree(preorder[mid + 1:],inorder[mid + 1:])
        return root

        