# level order traversal from dfs

'''
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right 
        self.left = left
'''

def level_order_dfs(root):
    result = []
    def dfs(node, depth):
        if not node:
            return
     # first node at this depth
        if depth == len(result):
            # open a bucket
            result.append([])
        result[depth].append(node.val)
        dfs(node.left,  depth + 1)
        dfs(node.right, depth + 1)
        
    dfs(root, 0)
    return result

# BST search (iterative)
def search_bst_iterative(root, target):
    node = root
    
    while node:
        if node.val == target:
            return node 
        
        # less than case 
        if node.val < target:
            node = node.left
        # otherwise 
        else:
            node = node.right
        
    return None

# BST inorder (iterative)
# we are keeping while node or stack since if there is a 
# stack we want to process the next item on the stack since that will be the 
# current node on display 
def inorder_iterative(root):
    result, stack = [], []
    node = root
 
    while node or stack:
        # dive left, remembering the way back
        while node:
            stack.append(node)
            node = node.left
 
        # the smallest unvisited node
        node = stack.pop()
        # process it
        result.append(node.val)
        # now handle its right subtree
        node = node.right
 
    return result